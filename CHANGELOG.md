# Changelog

## v1.1.0 (2026-10-25)

- GitHub Pages site: landing page with the spec scorer running fully in
  the browser (scorer.js, a port of spec_lint.py kept in sync by tests),
  live score, found and missing section lists, weak and full examples
- Dark mode on the site, following the system preference with a toggle

## v1.0.0 (2026-10-25)

Initial release.

- Five playbooks: the vibe PM loop, writing specs an AI can build,
  training vs tuning decision ladder, evals, launch and grow
- Six templates: PRD, spec, prompt brief, dataset card, eval scorecard,
  launch checklist
- tools/spec_lint.py: zero-dependency spec scorer with --check CI gate
  and --json output, 8 passing tests
- GOOD_FIRST_ISSUES.md with four seeded starter issues
