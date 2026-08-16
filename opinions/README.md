# opinions/ — Legal opinions & memos

Working analysis of counsel: questions the business asks, questions the
law raises. Not all memos are privileged — mark each file's front block
accordingly; privileged memos follow the disputes-level handling rules
(no cross-repo summaries).

## Memo format (binding)

```markdown
# Memo: <title>
Date: YYYY-MM-DD · Author: <role> · Privilege: privileged | internal
Question: <one sentence>
Short answer: <two sentences max>
Analysis: <reasoning, citations to instrument + article>
Action items: <owner + due date>
```

## Structure

- `YYYY/` — memos by year: `YYYY-MM-DD-<slug>.md`.
- `_index.md` — searchable index by topic; updated when a memo lands.

Topics expected early: deemed-supplier VAT analysis, AI Act chatbot
classification, processor-vs-controller role for institutional deals,
sacred-goods withdrawal-exception boundaries.

Memos that settle a position feed the affected artifact (clause library,
legal text, platform-regulation memo) in the same PR.
