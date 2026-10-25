# The vibe PM loop

Vibe coding changes who writes the code. It does not change what product
management is: deciding what to build, proving it works, and learning fast.
This loop is the kit's core workflow, one pass per feature.

## 1. Frame the problem
Write the problem before any solution. Who hurts, how often, what it costs
them. Use templates/prd-template.md. If you cannot state the problem in
two sentences, you are not ready to prompt anything.

## 2. Spec the slice
Turn the PRD into a buildable spec with templates/spec-template.md, then
score it: `python tools/spec_lint.py your-spec.md --check`. Below 70,
the AI builder will invent the missing parts, and invented scope is where
vibe projects go to die.

## 3. Brief the build
One slice per prompt session. Use templates/prompt-brief-template.md:
context, the exact output shape, the quality bar, and what to do when
information is missing. Long wish lists produce shallow code.

## 4. Build in slices, review like an engineer
Each slice ends working end to end, even if small. Review the diff the way
you would review a junior engineer's PR: run it, break it, read the parts
that touch data, money, or auth line by line.

## 5. Eval the behaviour
Anything the model decides needs an eval set before it ships: fixed inputs,
expected outputs, a pass gate. Use templates/eval-scorecard-template.md and
docs/04-evals.md. Vibes are not a test strategy.

## 6. Ship small, watch the guardrails
Release to the smallest audience that gives real signal. Watch the one
launch metric and the guardrail metric from the spec. Write down what you
learned while it is still true.

## 7. Feed the loop
Real usage becomes next round's evidence, eval cases, and, when the ladder
in docs/03-training-vs-tuning.md says so, training data. Most products
should stay on the early rungs of that ladder for a long time.

## Cadence that works
- Daily: one slice built and reviewed
- Per feature: one spec, one eval pass, one launch checklist
- Weekly: metrics review against the specs you shipped
- Monthly: prune the roadmap against what the metrics actually said
