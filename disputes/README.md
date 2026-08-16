# disputes/ — Disputes & litigation (HIGHEST RESTRICTION)

**Privilege doctrine:** access = GC + retained counsel only. Material in
this tree is work product prepared in anticipation of or during dispute
resolution. **No summaries, paraphrases, or status details from this tree
may appear in any other repository, issue tracker, dashboard, or chat.**
Cross-repo references use the matter id only
(e.g., "see matter D-2026-003 via GC").

## Structure

| Path | Contents |
|------|----------|
| `active/` | Live matters — one folder per matter |
| `pre-litigation/` | Demand letters (in/out), takedown escalations, escalated seller disputes |
| `closed/` | Archived matters + outcome register (feeds risk register) |
| `_register.md` | Matter index (minimal fields; substance stays in matter folders) |

## Matter lifecycle

1. **Open:** `_register.md` row + matter folder `<YYYY>-<NN>-<slug>/` with
   `intake.md` (category-level description only), counsel assignment,
   legal hold note.
2. **Run:** strategy, evidence index, correspondence — all inside the
   matter folder; evidence originals stay in DMS custody (index holds
   pointers).
3. **Close:** outcome note, costs, lessons; folder moves to `closed/`;
   outcome register row added; aggregated lesson fed to
   `jol-m-compliance/risk-register` (non-privileged phrasing only).

## Hard rules

- Settlement posture files never leave the matter folder.
- Insurance notice requirements (see `insurance/`) are checked at intake
  of every matter — late notice can void coverage.
- Personal data in matter files: minimize; claimant identities are
  load-bearing, everything else by pointer.
