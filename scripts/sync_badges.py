#!/usr/bin/env python3
"""
Sync badge-data-mainnet.json, badge-data-mainnet-protocols.json,
badge-data-superchain.json, and (when present) badge-data-part3.json
against the numbers that README.md itself actually states, so the
shields.io badges never silently go stale.

Deterministic, no LLM, no external API. Pure text parsing + JSON rewrite
+ optional git commit/push.

Source of truth in README.md:
  - Mainnet identity count: the "N addresses hold signer power on 2+
    independent protocols" sentence.
  - Mainnet / Superchain / Part 3 protocol counts: the "Protocols
    checked" row of the "At a glance" markdown table, 1st/2nd/3rd data
    columns respectively. Each column only needs to start with the
    digits; trailing text like "86 (12 on Arbitrum, 74 across 10
    further chains)" is fine, only the leading number is used.

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
from typing import NamedTuple, Optional

README_NAME = "README.md"
MAINNET_BADGE = "badge-data-mainnet.json"
MAINNET_PROTOCOLS_BADGE = "badge-data-mainnet-protocols.json"
SUPERCHAIN_BADGE = "badge-data-superchain.json"
PART3_BADGE = "badge-data-part3.json"

# "8 addresses hold signer power on 2+ independent protocols, ..."
MAINNET_PATTERN = re.compile(
    r"(\d+)\s+addresses hold signer power on\s+\d+\+?\s+independent protocols",
    re.IGNORECASE,
)

# At-a-glance table row, e.g.:
#   "| Protocols checked | 132 | 79 | 86 (12 on Arbitrum, 74 across 10 further chains) |"
# Captures everything between the row label and the trailing "|", then
# each data column is split out and read for its leading number so extra
# parenthetical detail in a cell doesn't break parsing.
ROW_PATTERN = re.compile(
    r"^\|\s*Protocols checked\s*\|(.*)\|\s*$",
    re.IGNORECASE | re.MULTILINE,
)

LEADING_INT_PATTERN = re.compile(r"\s*(\d+)")


def _leading_int(cell: str) -> Optional[str]:
    m = LEADING_INT_PATTERN.match(cell)
    return m.group(1) if m else None


class ParsedCounts(NamedTuple):
    mainnet_identities: str
    mainnet_protocols: str
    superchain_protocols: str
    part3_protocols: Optional[str]


def parse_readme(readme_text: str) -> ParsedCounts:
    """Return the counts the badges should reflect.

    part3_protocols is None when the table doesn't have a 3rd data
    column yet (2-part README), which is not an error.
    """
    mainnet_match = MAINNET_PATTERN.search(readme_text)
    if not mainnet_match:
        raise ValueError(
            "Could not find the 'N addresses hold signer power on 2+ "
            "independent protocols' sentence in README.md"
        )
    mainnet_identities = mainnet_match.group(1)

    row_match = ROW_PATTERN.search(readme_text)
    if not row_match:
        raise ValueError(
            "Could not find the 'Protocols checked' row of the At a "
            "glance table in README.md"
        )
    cells = row_match.group(1).split("|")
    if len(cells) < 2:
        raise ValueError(
            "'Protocols checked' row did not have the expected Mainnet "
            "and Superchain columns"
        )

    mainnet_protocols = _leading_int(cells[0])
    if mainnet_protocols is None:
        raise ValueError(
            "Could not parse a Mainnet protocol count from the "
            "'Protocols checked' row"
        )

    superchain_protocols = _leading_int(cells[1])
    if superchain_protocols is None:
        raise ValueError(
            "Could not parse a Superchain protocol count from the "
            "'Protocols checked' row"
        )

    part3_protocols = _leading_int(cells[2]) if len(cells) > 2 else None

    return ParsedCounts(
        mainnet_identities, mainnet_protocols, superchain_protocols, part3_protocols
    )


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
    mainnet_protocols_path = repo_root / MAINNET_PROTOCOLS_BADGE
    superchain_path = repo_root / SUPERCHAIN_BADGE
    part3_path = repo_root / PART3_BADGE

    for p in (readme_path, mainnet_path, mainnet_protocols_path, superchain_path):
        if not p.is_file():
            print(f"ERROR: expected file not found: {p}", file=sys.stderr)
            return 1

    readme_text = readme_path.read_text(encoding="utf-8")

    try:
        counts = parse_readme(readme_text)
    except ValueError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 1

    mainnet_current = load_badge_message(mainnet_path)
    mainnet_protocols_current = load_badge_message(mainnet_protocols_path)
    superchain_current = load_badge_message(superchain_path)

    print(f"README says mainnet identity count = {counts.mainnet_identities} "
          f"(badge currently says {mainnet_current})")
    print(f"README says Mainnet protocol count = {counts.mainnet_protocols} "
          f"(badge currently says {mainnet_protocols_current})")
    print(f"README says Superchain protocol count = {counts.superchain_protocols} "
          f"(badge currently says {superchain_current})")

    changed_files: list[Path] = []

    if mainnet_current != counts.mainnet_identities:
        print(f"MISMATCH: {MAINNET_BADGE} message '{mainnet_current}' "
              f"-> '{counts.mainnet_identities}'")
        if not args.dry_run:
            write_badge_message(mainnet_path, counts.mainnet_identities)
        changed_files.append(mainnet_path)

    if mainnet_protocols_current != counts.mainnet_protocols:
        print(f"MISMATCH: {MAINNET_PROTOCOLS_BADGE} message "
              f"'{mainnet_protocols_current}' -> '{counts.mainnet_protocols}'")
        if not args.dry_run:
            write_badge_message(mainnet_protocols_path, counts.mainnet_protocols)
        changed_files.append(mainnet_protocols_path)

    if superchain_current != counts.superchain_protocols:
        print(f"MISMATCH: {SUPERCHAIN_BADGE} message '{superchain_current}' "
              f"-> '{counts.superchain_protocols}'")
        if not args.dry_run:
            write_badge_message(superchain_path, counts.superchain_protocols)
        changed_files.append(superchain_path)

    # Part 3 badge is optional: only acted on when the README's table
    # actually has a 3rd data column AND badge-data-part3.json exists.
    # Neither missing is an error, it just means Part 3 isn't live yet.
    if counts.part3_protocols is not None and part3_path.is_file():
        part3_current = load_badge_message(part3_path)
        print(f"README says Part 3 protocol count = {counts.part3_protocols} "
              f"(badge currently says {part3_current})")
        if part3_current != counts.part3_protocols:
            print(f"MISMATCH: {PART3_BADGE} message '{part3_current}' "
                  f"-> '{counts.part3_protocols}'")
            if not args.dry_run:
                write_badge_message(part3_path, counts.part3_protocols)
            changed_files.append(part3_path)

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
