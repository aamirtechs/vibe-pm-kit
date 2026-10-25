# Writing specs an AI can build

An AI coding agent is a fast, literal, amnesiac engineer. It builds
exactly what the spec says, forgets yesterday's session, and fills every
gap with a plausible guess. Great specs for AI builders are boring in the
right places.

## The rules

1. **Name the observable result.** "User can export a CSV of this month's
   invoices" beats "add export functionality". If a person cannot verify
   it in five minutes, it is not a criterion yet.
2. **Write the non-goals.** The single highest-leverage section. Every
   unstated boundary becomes scope the model invents for you.
3. **Specify states, not just screens.** Empty, loading, error, partial,
   and permission-denied states are where generated apps look unfinished.
4. **Pin the allowed tools.** Stack, libraries, and conventions the model
   may use, and the ones it must not. Unpinned choices change every
   session and the codebase drifts.
5. **Give one example over ten adjectives.** A sample input and output, a
   screenshot description, a real record with private values removed.
6. **State the data rules.** Where data lives, what is sensitive, what
   must never be logged or sent to a model. Models are helpful; they will
   happily paste a secret into a fixture if the spec stays silent.
7. **Slice it.** A spec an agent can finish in one session stays coherent.
   If the spec needs the word "also" five times, split it.

## Anti-patterns

- The novel: 4,000 words of vision, zero acceptance criteria
- The wishlist: forty features, no priorities, no non-goals
- The screenshot-only brief: a picture with no behaviour behind it
- The moving target: editing the spec mid-build instead of versioning it

## Check yourself

Run the kit's linter on every spec before building:

```bash
python tools/spec_lint.py path/to/spec.md --check --min-score 70
```

Then read the spec once as the model will: literally, with no memory of
your intentions. Fix what that reader would get wrong.
