import json
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import spec_lint  # noqa: E402

COMPLETE_SPEC = """# Widget

## Problem
Users waste time.

## Target users
Solo founders.

## Goals and scope
Ship an MVP.

## Non-goals
No mobile app.

## Workflows
User signs up, then exports.

## Acceptance criteria
Export produces a CSV.

## Data and models
No training data. Prompting only, no fine-tuning.

## Risks
API downtime.

## Success metrics
Activation rate.
"""

EMPTY_SPEC = "# Untitled\n\nSome thoughts.\n"


class LintTextTests(unittest.TestCase):
    def test_complete_spec_scores_100(self):
        report = spec_lint.lint_text(COMPLETE_SPEC)
        self.assertEqual(report["score"], 100)
        self.assertEqual(report["missing"], [])

    def test_empty_spec_scores_low(self):
        report = spec_lint.lint_text(EMPTY_SPEC)
        self.assertLess(report["score"], 30)
        self.assertIn("Problem", report["missing"])

    def test_partial_spec_reports_missing_sections(self):
        report = spec_lint.lint_text("## Problem\nX.\n\n## Risks\nY.\n")
        self.assertIn("Problem", report["found"])
        self.assertIn("Non-goals", report["missing"])

    def test_synonyms_match(self):
        report = spec_lint.lint_text("## Who is it for\nFounders.\n\n## Out of scope\nNothing yet.\n")
        self.assertIn("Target users", report["found"])
        self.assertIn("Non-goals", report["found"])

    def test_bold_labels_match(self):
        report = spec_lint.lint_text("**Problem**\nIt hurts.\n")
        self.assertIn("Problem", report["found"])


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        return subprocess.run(
            [sys.executable, str(ROOT / "tools" / "spec_lint.py"), *args],
            capture_output=True, text=True)

    def test_template_scores_100(self):
        template = ROOT / "templates" / "spec-template.md"
        result = self.run_cli(str(template), "--json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(json.loads(result.stdout)["score"], 100)

    def test_check_fails_below_min_score(self):
        bad = ROOT / "tests" / "_bad_spec.md"
        bad.write_text(EMPTY_SPEC, encoding="utf-8")
        try:
            result = self.run_cli(str(bad), "--check")
            self.assertEqual(result.returncode, 1)
        finally:
            bad.unlink()

    def test_missing_file_exit_2(self):
        result = self.run_cli("does-not-exist.md")
        self.assertEqual(result.returncode, 2)


if __name__ == "__main__":
    unittest.main()
