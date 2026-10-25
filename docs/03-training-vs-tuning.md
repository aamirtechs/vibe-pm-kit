# Training vs tuning: the decision ladder

Most "we need to train a model" conversations end three rungs earlier on
this ladder. Climb only when the rung below measurably fails, and prove
each step with the eval scorecard, not with taste.

## The ladder

| Rung | Move | Cost | Reach for it when |
|---|---|---|---|
| 1 | Better prompts | Hours | Always start here. Most quality problems are instruction problems. |
| 2 | Few-shot examples | Hours | Output shape or tone is inconsistent and examples fix it. |
| 3 | RAG (retrieval) | Days | The model needs your facts: docs, prices, policies, inventory. Facts change, so retrieve them instead of memorising them. |
| 4 | Fine-tuning | Days to weeks, plus data work | Format, style, or classification behaviour must be consistent at scale, and prompts plus examples plateau on the eval set. |
| 5 | Training from scratch | Months, serious budget | Almost never for product teams. Justifiable for a new modality, a licence-clean base, or research, not for an app feature. |

## Fine-tuning, honestly

Fine-tuning changes behaviour, not knowledge. It is good at tone, format,
label sets, and domain phrasing. It is bad at facts, which go stale, and
it cannot fix a broken product flow. Budget honestly: the model run is
the cheap part. The expensive part is a clean, consented, labelled
dataset, and every future refresh of it.

Before any fine-tune, you need:
- An eval set that already exists (build it at rung 1, not after)
- At least a few hundred high-quality examples, more for open-ended tasks
- A dataset card (templates/dataset-card-template.md) covering source,
  consent, PII handling, and known gaps
- A rollback plan: the previous prompt or model stays deployable

## Training from scratch, honestly

Pretraining buys you a base model, not a product. Unless your product is
the model itself, the capital, data, and eval burden belong to a research
program. Product teams get more from a strong base model, good retrieval,
and disciplined evals than from owning weights.

## Data hygiene rules for every rung

- Never train or tune on data you do not have the right to use
- Remove or mask PII before data touches a training pipeline, and verify
  the masking on samples, not by trusting the script
- Keep a held-out test split the tuning process never sees
- Version datasets like code; an unversioned dataset makes every result
  unrepeatable
- Synthetic data is fine for shape and coverage, dangerous for facts;
  label it as synthetic in the dataset card
