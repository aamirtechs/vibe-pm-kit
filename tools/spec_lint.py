#!/usr/bin/env python3
"""spec-lint: score a product spec written for AI-assisted building.

Vibe coding fails most often at the spec, not the code. This tool checks a
Markdown spec for the sections an AI builder (or a human engineer) needs
before writing code: the problem, the users, scope, explicit non-goals,
workflows, acceptance criteria, data and model notes, risks, and success
metrics. It prints a score out of 100 and can gate CI with --check.

Zero dependencies. Python 3.9+.
"""

import argparse
import json
import re
import sys

# Each required section: display name, weight, heading synonyms (lowercase).
SECTIONS = [
    ("Problem", 15, ["problem", "why", "motivation", "pain point"]),
    ("Target users", 10, ["target users", "users", "audience", "personas", "who is it for"]),
    ("Goals and scope", 15, ["goals and scope", "scope", "goals", "in scope", "requirements"]),
    ("Non-goals", 10, ["non-goals", "non goals", "out of scope", "not doing"]),
    ("Workflows", 10, ["workflows", "user stories", "user flow", "how it works", "journeys"]),
    ("Acceptance criteria", 15, ["acceptance criteria", "definition of done", "done when", "success criteria"]),
    ("Data and models", 10, ["data and models", "data", "models", "training", "tuning", "fine-tuning", "rag"]),
    ("Risks", 5, ["risks", "risk", "edge cases", "failure modes"]),
    ("Success metrics", 10, ["success metrics", "metrics", "kpis", "measurement", "how we measure"]),
]

MIN_HEADING_LEVEL = 1
MAX_HEADING_LEVEL = 4


def extract_headings(text):
    """Return the lowercase text of every Markdown heading."""
    headings = []
    for line in text.splitlines():
        m = re.match(r"^(#{1,6})\s+(.*)$", line.strip())
        if m and MIN_HEADING_LEVEL <= len(m.group(1)) <= MAX_HEADING_LEVEL + 2:
            headings.append(m.group(2).strip().lower())
    return headings


def lint_text(text):
    """Score spec text. Returns a dict with score, found and missing sections."""
    headings = extract_headings(text)
    body = text.lower()
    found, missing = [], []
    score = 0
    for name, weight, synonyms in SECTIONS:
        hit = any(syn in h for h in headings for syn in synonyms)
        if not hit:
            # Fall back to a bolded label or a plain mention near the top level.
            hit = any(re.search(r"^\s*(\*\*|__)" + re.escape(syn) + r"(\*\*|__)", body, re.M)
                      for syn in synonyms)
        if hit:
            found.append(name)
            score += weight
        else:
            missing.append(name)
    return {"score": score, "found": found, "missing": missing}


def lint_file(path):
    with open(path, encoding="utf-8") as fh:
        return lint_text(fh.read())


def main(argv=None):
    ap = argparse.ArgumentParser(description="Score a Markdown product spec for AI-assisted building.")
    ap.add_argument("spec", help="Path to the spec Markdown file")
    ap.add_argument("--json", action="store_true", help="Print the report as JSON")
    ap.add_argument("--check", action="store_true",
                    help="Exit 1 when the score is below --min-score (for CI)")
    ap.add_argument("--min-score", type=int, default=70,
                    help="Minimum passing score for --check (default 70)")
    args = ap.parse_args(argv)

    try:
        report = lint_file(args.spec)
    except OSError as exc:
        print(f"error: cannot read {args.spec}: {exc}", file=sys.stderr)
        return 2

    report = {"file": args.spec, **report}
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"Spec score: {report['score']}/100 for {args.spec}")
        for name in report["found"]:
            print(f"  ok       {name}")
        for name in report["missing"]:
            print(f"  MISSING  {name}")
        if report["missing"]:
            print("Tip: templates/spec-template.md in vibe-pm-kit covers every section.")

    if args.check and report["score"] < args.min_score:
        print(f"FAIL: score {report['score']} is below the minimum {args.min_score}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
