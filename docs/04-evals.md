# Evals: proving the model behaves

If a model decides anything in your product, you need an eval set. Not a
demo, not a feeling: a fixed set of inputs with expected outputs and a
pass gate, re-run on every change.

## Build the eval set first

1. Start with 20 to 50 real cases from real usage or support, with private
   values removed or replaced.
2. Add the edge cases that scare you: empty input, huge input, abusive
   input, ambiguous input, the competitor's name, the refund demand.
3. Write the expected output or the rule it must satisfy. For open-ended
   outputs, define the rule (contains X, never says Y, format Z).
4. Split: a tuning set you may iterate against, and a held-out set you
   only check before shipping.

## Grade like you mean it

- Exact or rule-based checks first: cheap, fast, repeatable
- A stronger model as judge second, with a written rubric, and only where
  rules cannot decide
- Human spot-checks always: 10 samples per run, read by a person, counted
  on the scorecard

## Gate the release

Decide the gates before you see the numbers (templates/eval-scorecard-template.md
has defaults): no drop in accuracy, zero critical hallucinations, full
format compliance, cost and latency inside budget. A change that fails a
gate does not ship, however good the demo looked.

## Keep evals alive

Every production failure becomes a new eval case the week it happens.
Every model or prompt version change re-runs the full set. Eval sets that
sit still quietly stop measuring the product you actually run.
