# DSA notice-and-action — Art. 16 reporting flow spec

**Regulation (EU) 2022/2065, Art. 16 (notice and action mechanisms).**

## Legal position

Anyone must be able to notify us of specific items they consider illegal
content. Notices sufficient to allow a diligent provider to act must
contain: substantiated explanation, exact location (URL/listing id),
notifier identity (name + email), and good-faith statement. Qualified
trusted flaggers (Art. 22, when applicable) get priority, non-abusive
processing.

## Product spec hook

1. Entry points: report button on listing/review/profile + dedicated
   channel (no login wall for reporting).
2. Intake form collecting the Art. 16(2) minimum set.
3. Acknowledgement of receipt **without undue delay** (Art. 16(5)).
4. Triage → decision → **statement of reasons** to notifier and affected
   trader (see `statement-of-reasons.md`).
5. Abuse handling: notices obviously abusive processed proportionally;
   suspension of frequent-abuse accounts documented.
6. Criminal-content escalation path to law enforcement (GC decision,
   counsel + security function).

## Metrics (transparency report inputs)

Notices received, by category, by outcome, median time-to-decision,
trusted-flagger share. Data lineage recorded per report cycle.

## Status

- [ ] Form fields approved by GC
- [ ] Triage SLAs defined with product
- [ ] Abuse thresholds documented (proportionality memo in opinions/)
