# Good first issues

Four small, self-contained starting points. Each states the file to
touch and what counts as done.

## 1. Add a --strict-headings mode to spec_lint

File: `tools/spec_lint.py`, tests in `tests/test_spec_lint.py`.

Today the linter also accepts bolded labels as sections. Add a
`--strict-headings` flag that only counts real Markdown headings.

Acceptance criteria:
- Default behaviour unchanged without the flag
- With the flag, a bold-label-only spec loses those sections
- At least two new tests cover both modes

## 2. Add a worked example spec to templates

File: new `templates/example-spec-todo-app.md`.

Write a complete, filled-in example spec for a small fictional product
(a team todo app with an AI prioritisation feature) that scores 100 with
spec_lint, so new users see what "done" looks like.

Acceptance criteria:
- Scores 100 via `python tools/spec_lint.py templates/example-spec-todo-app.md --check`
- The Data and models section makes a justified ladder choice
  (docs/03) instead of defaulting to fine-tuning
- Linked from the README templates list

## 3. Add a cost estimation worksheet

File: new `templates/cost-worksheet.md`.

A one-page worksheet for estimating per-user AI cost before launch:
calls per user per day, tokens in and out, price per token, caching
assumptions, and the 10x traffic line from the launch checklist.

Acceptance criteria:
- One filled fictional example included
- Every input is a number a PM can actually find
- Linked from docs/05-launch-and-grow.md

## 4. Translate the spec template

Files: new `templates/spec-template.<lang>.md`.

Translate templates/spec-template.md into another language, keeping the
English section headings (so spec_lint still scores it) and translating
the guidance text.

Acceptance criteria:
- The translated template still scores 100 with spec_lint
- A native speaker has reviewed it (say so in the PR)
- Linked from the README
