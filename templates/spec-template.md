# Spec: <product or feature name>

One line summary of what this is and who it serves.

## Problem

What hurts, for whom, and how do you know? Evidence beats opinion: quotes,
support tickets, numbers. One short paragraph plus the evidence.

## Target users

Primary persona, secondary persona, and who this is explicitly not for.

## Goals and scope

- Goal 1 (outcome, not output)
- Goal 2
- In scope for this version: the smallest slice that proves the idea

## Non-goals

- Thing we are deliberately not building now, and why
- Thing people will ask for that belongs to a later version

## Workflows

1. The happy path, step by step, in the order the user lives it
2. The empty state (first run, no data yet)
3. The error path (what the user sees when something fails)

## Acceptance criteria

- [ ] Given <context>, when <action>, then <observable result>
- [ ] Works with the sample data in the repo or the brief
- [ ] No placeholder text, dead buttons, or TODO screens in the shipped slice

## Data and models

- Data sources and where they live (never paste secrets into a spec)
- Approach: prompting / few-shot / RAG / fine-tuning / training, and why
  (see docs/03-training-vs-tuning.md for the decision ladder)
- Eval set: where the test cases live and what passing means

## Risks

- The most likely way this fails in production
- The most expensive way this fails
- Abuse, privacy, or cost risks and the mitigation for each

## Success metrics

- The one metric that decides whether this ships wider
- The guardrail metric that must not get worse
- When we review them (date or milestone)
