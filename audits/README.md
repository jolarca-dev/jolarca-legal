# audits/ — Internal audit records for this repository

Periodic self-checks of the legal repository's own controls, kept apart
from the material they audit.

| Audit | Cadence | Checks |
|-------|---------|---------|
| Access review | quarterly | repo collaborators vs. need-to-have; privileged-path grants; stale access revocation |
| Register integrity | quarterly | every executed vendor folder has a register row; schema intact |
| Legal-text sync audit | quarterly | product-pinned versions match published manifest; consent registry consistent |
| Retention sweep | annual | retention-schedule.md deadlines executed; holds respected |
| Renewal-window audit | annual | no missed notice windows (contract + IP + insurance); misses are findings |

Files: `internal/YYYY-MM-<audit>.md` — scope, findings, remediation
owner, close date. Findings feed `jolarca-compliance/risk-register` in
non-privileged phrasing.
