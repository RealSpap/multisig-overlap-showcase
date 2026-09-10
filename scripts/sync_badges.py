#!/usr/bin/env python3
"""
Sync badge-data-mainnet.json and badge-data-superchain.json against the
numbers that README.md itself actually states, so the shields.io badges
never silently go stale.

Deterministic, no LLM, no external API. Pure text parsing + JSON rewrite
+ optional git commit/push.

Source of truth in README.md:
  - Mainnet identity count: the "N addresses hold signer power on 2+
    independent protocols" sentence.
  - Superchain protocol count: the "Protocols checked" row of the
    "At a glance" markdown table, Superchain column.

Usage:
  python3 sync_badges.py [--repo-root PATH] [--no-commit] [--no-push] [--dry-run]

Exit codes:
  0  ran successfully (whether or not a change was made)
  1  could not parse one of the expected values out of README.md
  2  git commit/push failed
"""

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

README_NAME = "README.md"
MAINNET_BADGE = "badge-data-mainnet.json"
SUPERCHAIN_BADGE = "badge-data-superchain.json"

# "8 addresses hold signer power on 2+ independent protocols, ..."
MAINNET_PATTERN = re.compile(
    r"(\d+)\s+addresses hold signer power on\s+\d+\+?\s+independent protocols",
    re.IGNORECASE,
)

# At-a-glance table row: "| Protocols checked | 41 | 79 |"
# Group 1 = Mainnet column, group 2 = Superchain column.
SUPERCHAIN_PATTERN = re.compile(
    r"^\|\s*Protocols checked\s*\|\s*(\d+)\s*\|\s*(\d+)\s*\|\s*$",
    re.IGNORECASE | re.MULTILINE,
)


def parse_readme(readme_text: str) -> tuple[str, str]:
    """Return (mainnet_identity_count, superchain_protocol_count) as strings."""
    mainnet_match = MAINNET_PATTERN.search(readme_text)
    if not mainnet_match:
        raise ValueError(
            "Could not find the 'N addresses hold signer power on 2+ "
            "independent protocols' sentence in README.md"
        )
    mainnet_count = mainnet_match.group(1)

    superchain_match = SUPERCHAIN_PATTERN.search(readme_text)
    if not superchain_match:
        raise ValueError(
            "Could not find the 'Protocols checked' row of the At a "
            "glance table in README.md"
        )
    superchain_count = superchain_match.group(2)

    return mainnet_count, superchain_count


def load_badge_message(path: Path) -> str:
    data = json.loads(path.read_text(encoding="utf-8"))
    return str(data.get("message", ""))


def write_badge_message(path: Path, new_message: str) -> None:
    data = json.loads(path.read_text(encoding="utf-8"))
    data["message"] = new_message
    # Keep shields.io schema key order stable and end with a trailing
    # newline, matching typical hand-authored JSON in this repo.
    path.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")


def run(cmd: list[str], cwd: Path) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--repo-root",
        default=".",
        help="Path to the repo checkout containing README.md and the badge files.",
    )
    parser.add_argument(
        "--no-commit",
        action="store_true",
        help="Rewrite JSON files if needed but do not git commit.",
    )
    parser.add_argument(
        "--no-push",
        action="store_true",
        help="Commit locally if needed but do not git push.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only report what would change; do not write files or touch git.",
    )
    args = parser.parse_args()

    repo_root = Path(args.repo_root).resolve()
    readme_path = repo_root / README_NAME
    mainnet_path = repo_root / MAINNET_BADGE
    superchain_path = repo_root / SUPERCHAIN_BADGE

    for p in (readme_path, mainnet_path, superchain_path):
        if not p.is_file():
            print(f"ERROR: expected file not found: {p}", file=sys.stderr)
            return 1

    readme_text = readme_path.read_text(encoding="utf-8")

    try:
        mainnet_expected, superchain_expected = parse_readme(readme_text)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    mainnet_current = load_badge_message(mainnet_path)
    superchain_current = load_badge_message(superchain_path)

    print(f"README says mainnet identity count = {mainnet_expected} "
          f"(badge currently says {mainnet_current})")
    print(f"README says Superchain protocol count = {superchain_expected} "
          f"(badge currently says {superchain_current})")

    changed_files: list[Path] = []

    if mainnet_current != mainnet_expected:
        print(f"MISMATCH: {MAINNET_BADGE} message '{mainnet_current}' "
              f"-> '{mainnet_expected}'")
        if not args.dry_run:
            write_badge_message(mainnet_path, mainnet_expected)
        changed_files.append(mainnet_path)

    if superchain_current != superchain_expected:
        print(f"MISMATCH: {SUPERCHAIN_BADGE} message '{superchain_current}' "
              f"-> '{superchain_expected}'")
        if not args.dry_run:
            write_badge_message(superchain_path, superchain_expected)
        changed_files.append(superchain_path)

    if not changed_files:
        print("Badges already match README.md. Nothing to do.")
        return 0

    if args.dry_run:
        print("Dry run: not writing files or committing.")
        return 0

    print(f"Updated {len(changed_files)} file(s): "
          f"{', '.join(p.name for p in changed_files)}")

    if args.no_commit:
        print("--no-commit set: leaving changes uncommitted.")
        return 0

    try:
        run(["git", "config", "user.name", "badge-sync-bot"], repo_root)
        run(["git", "config", "user.email",
             "badge-sync-bot@users.noreply.github.com"], repo_root)
        run(["git", "add"] + [str(p.relative_to(repo_root)) for p in changed_files],
            repo_root)

        # Guard against a no-op commit even if content ended up identical
        # to HEAD for some reason (e.g. re-run after a manual fix).
        diff = subprocess.run(
            ["git", "diff", "--cached", "--quiet"], cwd=repo_root
        )
        if diff.returncode == 0:
            print("No staged changes after write (already matched HEAD). "
                  "Skipping commit.")
            return 0

        names = ", ".join(p.name for p in changed_files)
        run(["git", "commit", "-m", f"chore: sync badge data with README ({names})"],
            repo_root)
        print("Committed badge sync.")

        if args.no_push:
            print("--no-push set: leaving commit unpushed.")
            return 0

        run(["git", "push"], repo_root)
        print("Pushed badge sync commit.")
    except subprocess.CalledProcessError as exc:
        print(f"ERROR: git command failed: {exc.cmd}", file=sys.stderr)
        print(exc.stdout, file=sys.stderr)
        print(exc.stderr, file=sys.stderr)
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
