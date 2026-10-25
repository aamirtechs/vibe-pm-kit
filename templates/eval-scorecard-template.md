# Eval scorecard: <model or feature name>

Run the same eval set before and after every prompt change, fine-tune, or
model swap. Record numbers, not impressions.

| Field | Value |
|---|---|
| Date | |
| Model and version | |
| Prompt or config version | |
| Eval set version | |
| Changed by | |

## Results

| Metric | Before | After | Gate |
|---|---|---|---|
| Accuracy on eval set (%) | | | must not drop |
| Hallucination or invented-fact cases | | | must be 0 on critical cases |
| Format compliance (%) | | | 100 |
| Median latency | | | within budget |
| Cost per 1,000 runs | | | within budget |
| Human spot-check (10 samples, pass count) | | | 9 or more |

## Failures worth naming
List the worst three failures from this run, what caused them, and the fix
(a prompt change, more data, a rule, or an accepted limitation).

## Decision
Ship / iterate / roll back, and the one line of reasoning.
