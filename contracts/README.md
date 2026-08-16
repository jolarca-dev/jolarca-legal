# contracts/ — Contract Lifecycle Management (CLM)

All third-party and employment instruments, from draft to archive.

## Lifecycle

```
draft → redline → approved → executed → renewal/exit
```

- **draft** — JOL template or counterparty paper, in the instrument folder
- **redline** — negotiation rounds kept as `*-redline-*` artifacts;
  negotiation history is preserved (CONTRIBUTING.md §1)
- **approved** — GC sign-off recorded in the folder's `metadata.md`
- **executed** — folder marked executed; **content becomes immutable**;
  changes only via amendment/restatement documents
- **renewal/exit** — driven by the register + `contract-renewals.yml`
  (90/60/30-day tasks; notice deadlines are the hard constraint)

## Layout

| Path | Contents |
|------|----------|
| `00-templates/` | JOL-standard instruments + clause library reference |
| `vendors/` | Executed vendor contracts — one folder per vendor + `_register.csv` |
| `customers/` | Enterprise/institutional agreements (dioceses, funeral-home chains) |
| `partnerships/` | Channel & referral partners |
| `employment/` | Employment + contractor agreements (access-restricted) |
| `_clause-library.md` | Approved fallback positions for negotiation |

## The register (`vendors/_register.csv`)

Machine-readable contract index — parsed by `scripts/renewal-report.py`
and the renewal automation. Every executed vendor instrument **must** have
a register row the day it executes; the compliance gate checks this rule.
Schema is fixed (see the register header); customers/partnerships keep
their own `_register.csv` per the same schema as they land.

## Per-instrument folder convention

```
vendors/<counterparty>/
├── metadata.md          # counterparty, instrument class, owner,
│                        #   status, executed date, custody pointer (DMS ref)
├── 2026-04-01-msa.md    # negotiated text (or pointer for counterparty paper)
└── 2026-04-01-dpa.md    # related instruments (DPA, schedules)
```

Signed originals live in the document-management custody location —
`metadata.md` carries the pointer, never the scan cache.

## Intake

New contract requests start as issues (`contract_request.yml`); legal
re-classifies risk tier and routes to the right template.
