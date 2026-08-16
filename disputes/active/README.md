# active/ — Live matters

One folder per matter: `YYYY-NN-slug/`.

Standard contents:

- `intake.md` — received/opened date, counterparty, category, exposure
  tier, insurance-notified flag, counsel assigned.
- `strategy.md` — counsel direction; privileged.
- `evidence-index.md` — pointers to DMS custody items (never the items
  themselves where privileged/PII).
- `timeline.md` — dated procedural steps.
- `hold.md` — legal hold scope and custodians.

Rules: GC + retained counsel only (CODEOWNERS). Anything here is presumed
privileged; when in doubt, treat as privileged.
