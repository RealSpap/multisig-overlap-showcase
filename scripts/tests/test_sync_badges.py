"""scripts/sync_badges.py : the mainnet sentence moved from README.md to docs/part-1-mainnet.md on 2026-11-16 and the badge job broke.
Each case below is a planted fault or layout; the last test mutates the script and checks that each mutant is caught."""
import contextlib, importlib.util, io, json, shutil, sys, tempfile, unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE.parent / "sync_badges.py"


def load(src=None):
    spec = importlib.util.spec_from_file_location("sync_badges_under_test", SCRIPT)
    mod = importlib.util.module_from_spec(spec)
    if src is None:
        spec.loader.exec_module(mod)
    else:
        exec(compile(src, "sync_badges_mutant", "exec"), mod.__dict__)
    return mod


SENT = "8 addresses hold signer power on 2+ independent protocols, sorted by reach.\n"
TABLE = "| | A | B | C | Total |\n|---|---|---|---|---|\n| Protocols checked | 214 | 105 | 109 (across 11 chains) | 428 (sum) |\n"
BADGES = {"badge-data-mainnet.json": "8", "badge-data-mainnet-protocols.json": "214", "badge-data-superchain.json": "105",
          "badge-data-part3.json": "109", "badge-data-total.json": "428"}


def make_repo(readme, part1=None, badges=BADGES):
    d = Path(tempfile.mkdtemp())
    (d / "README.md").write_text(readme, encoding="utf-8")
    if part1 is not None:
        (d / "docs").mkdir()
        (d / "docs" / "part-1-mainnet.md").write_text(part1, encoding="utf-8")
    for name, msg in badges.items():
        (d / name).write_text(json.dumps({"schemaVersion": 1, "label": "x", "message": msg, "color": "green"}), encoding="utf-8")
    return d


def run_main(mod, d, *flags):
    err, out = io.StringIO(), io.StringIO()
    old = sys.argv
    sys.argv = ["sync_badges.py", "--repo-root", str(d), *flags]
    try:
        with contextlib.redirect_stderr(err), contextlib.redirect_stdout(out):
            code = mod.main()
    finally:
        sys.argv = old
    return code, out.getvalue(), err.getvalue()


class SyncBadges(unittest.TestCase):
    mod = None

    def setUp(self):
        self.m = self.mod or load()
        self.dirs = []

    def tearDown(self):
        for d in self.dirs:
            shutil.rmtree(d, ignore_errors=True)

    def repo(self, *a, **k):
        d = make_repo(*a, **k)
        self.dirs.append(d)
        return d

    def test_sentence_only_in_the_docs_file_is_found(self):  # the real regression of 2026-11-16
        self.assertEqual(self.m.parse_readme(TABLE, SENT).mainnet_identities, "8")

    def test_sentence_only_in_the_readme_is_still_found(self):
        self.assertEqual(self.m.parse_readme(SENT + TABLE).mainnet_identities, "8")

    def test_sentence_nowhere_is_an_error(self):
        with self.assertRaises(ValueError):
            self.m.parse_readme(TABLE, "nothing here\n")

    def test_two_different_numbers_are_an_error_not_a_pick(self):
        with self.assertRaises(ValueError):
            self.m.parse_readme(SENT + TABLE, SENT.replace("8", "9", 1))

    def test_same_number_twice_is_fine(self):
        self.assertEqual(self.m.parse_readme(SENT + TABLE, SENT).mainnet_identities, "8")

    def test_run_exit_codes_on_a_split_readme(self):
        ok = self.repo(TABLE, SENT)
        self.assertEqual(run_main(self.m, ok, "--dry-run")[0], 0)
        broken = self.repo(TABLE, "no sentence\n")
        code, _, err = run_main(self.m, broken, "--dry-run")
        self.assertEqual(code, 1)
        self.assertIn("sentence", err)

    def test_old_layout_without_a_docs_file_still_runs(self):  # sentence in the README, no docs/ directory at all
        d = self.repo(SENT + TABLE)
        self.assertEqual(run_main(self.m, d, "--dry-run")[0], 0)

    def test_stale_badge_is_rewritten_from_the_docs_sentence(self):
        d = self.repo(TABLE, SENT.replace("8", "9", 1))
        code, out, _ = run_main(self.m, d, "--no-commit")
        self.assertEqual(code, 0)
        self.assertEqual(json.loads((d / "badge-data-mainnet.json").read_text())["message"], "9")
        self.assertIn("MISMATCH", out)


MUTANTS = [
    ('mainnet_identities = find_mainnet_identities(readme_text, part1_text)', 'mainnet_identities = find_mainnet_identities(readme_text)'),
    ('if len(found) > 1:', 'if False:'),
    ('if not found:', 'if False:'),
    ('part1_text = part1_path.read_text(encoding="utf-8") if part1_path.is_file() else ""', 'part1_text = ""'),
    ('part1_text = part1_path.read_text(encoding="utf-8") if part1_path.is_file() else ""', 'part1_text = part1_path.read_text(encoding="utf-8")'),
    ('counts = parse_readme(readme_text, part1_text)', 'counts = parse_readme(readme_text, "")'),
]


class Mutants(unittest.TestCase):
    def test_every_mutant_is_caught(self):
        src = SCRIPT.read_text(encoding="utf-8")
        alive = []
        for old, new in MUTANTS:
            self.assertEqual(src.count(old), 1, "mutant has no hold: %r" % old)
            SyncBadges.mod = load(src.replace(old, new))
            try:
                res = unittest.TestResult()
                unittest.defaultTestLoader.loadTestsFromTestCase(SyncBadges).run(res)
                caught = bool(res.failures or res.errors)
            except Exception:  # a mutant that crashes is caught
                caught = True
            finally:
                SyncBadges.mod = None
            if not caught:
                alive.append(old)
        self.assertEqual(alive, [])


if __name__ == "__main__":
    unittest.main()
