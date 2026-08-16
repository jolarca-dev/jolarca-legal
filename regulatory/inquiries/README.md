# inquiries/ — Authority inquiries (PRIVILEGED)

**Privilege doctrine:** every file in this folder is treated as
privileged from the moment of intake — prepared for counsel / under
counsel direction. Access = GC + retained counsel only (CODEOWNERS).
No summaries of this folder may appear in any other repository, issue,
dashboard, or chat. If another team needs to know status, the answer is
the matter id and the GC's contact — nothing else.

## Intake → counsel → response → closure

1. **Intake (same day):** file `<YYYY>-INQ-<NN>/intake.md` — authority,
   received date, statutory deadline, subject (category only, no
   substance), handler.
2. **Counsel engagement (≤ 1 business day):** retained counsel noted in
   the folder; all further drafting happens under their direction.
3. **Response:** drafts live in the matter folder only; sent version
   archived with dispatch proof.
4. **Closure:** outcome note + feed to `jol-m-compliance/risk-register`
   (aggregated, non-privileged) + retention per `docs/retention-schedule.md`.

## Legal hold

Opening a matter folder triggers legal hold for related records
(contracts, logs, correspondence). Hold scope is recorded in
`<matter>/hold.md`; releases only by GC + counsel.
