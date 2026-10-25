# vibe-pm-kit

[![GitHub stars](https://img.shields.io/github/stars/aamirtechs/vibe-pm-kit?style=social)](https://github.com/aamirtechs/vibe-pm-kit/stargazers) [![GitHub forks](https://img.shields.io/github/forks/aamirtechs/vibe-pm-kit?style=social)](https://github.com/aamirtechs/vibe-pm-kit/network/members) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE) [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/aamirtechs/vibe-pm-kit/pulls)

**The product management kit for vibe coding.** Specs an AI can build,
prompt briefs, eval scorecards, and honest playbooks for training and
tuning models, plus a zero-dependency spec linter that scores your spec
before you build from it.

**Live site: https://aamirtechs.github.io/vibe-pm-kit/** with the spec
scorer running in your browser. Paste a spec, get the score, fix the gaps.

Vibe coding made building fast. It did not make deciding what to build,
proving the model behaves, or knowing when to fine-tune any easier. This
kit is the missing product layer: small, practical, and opinionated.

## Quickstart

Score the included spec template (it scores 100):

```bash
python tools/spec_lint.py templates/spec-template.md --check
```

Then score your own spec before your next build session:

```bash
python tools/spec_lint.py path/to/your-spec.md
```

Example output:

```text
Spec score: 55/100 for my-spec.md
  ok       Problem
  ok       Target users
  ok       Goals and scope
  ok       Workflows
  ok       Risks
  MISSING  Non-goals
  MISSING  Acceptance criteria
  MISSING  Data and models
  MISSING  Success metrics
```

## What's inside

**Playbooks (docs/)**
- [The vibe PM loop](docs/01-the-vibe-pm-loop.md): frame, spec, brief,
  build, eval, ship, learn
- [Writing specs an AI can build](docs/02-writing-specs-ai-can-build.md):
  the rules and the anti-patterns
- [Training vs tuning](docs/03-training-vs-tuning.md): the decision
  ladder from prompts to RAG to fine-tuning to training, with the honest
  costs of each rung
- [Evals](docs/04-evals.md): building eval sets and gating releases on
  them
- [Launch and grow](docs/05-launch-and-grow.md): shipping and spreading
  a vibe-built product without spam tricks

**Templates (templates/)**
- PRD template, spec template, prompt brief template
- Dataset card template (fill before any training or tuning run)
- Eval scorecard template, launch checklist

**Tool (tools/)**
- `spec_lint.py`: zero-dependency Python CLI that checks a Markdown spec
  for the nine sections an AI builder needs and scores it out of 100,
  with `--check` and `--min-score` for CI

## Who this is for

- Solo founders and indie hackers building with AI coding agents
- Product managers whose team now ships with models in the loop
- Anyone who has watched a vibe-coded demo collapse on real data and
  wants the process that prevents it

## Tests

```bash
python -m pytest tests/ -q
# or
python -m unittest discover -s tests
```

## Contributing

Issues and PRs are welcome. GOOD_FIRST_ISSUES.md lists small, well-scoped
starting points. Keep additions practical: if a practising PM cannot use
it this week, it does not belong in the kit yet.

## License

MIT. Copyright 2026 Amir Hussain.
