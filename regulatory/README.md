# regulatory/ — Authorities & correspondence

## Authority map

| Authority | Jurisdiction | Domain | Folder |
|-----------|--------------|--------|--------|
| VDAI (Valstybinė duomenų apsaugos inspekcija) | LT | Data protection | `supervisory-authorities/` |
| DVI (Datu valsts inspekcija) | LV | Data protection | `supervisory-authorities/` |
| AKI (Andmekaitse Inspektsioon) | EE | Data protection | `supervisory-authorities/` |
| State Consumer Rights Protection Authority (VVTAT) | LT | Consumer protection | `consumer-protection/` |
| PTAC | LV | Consumer protection | `consumer-protection/` |
| TTJA | EE | Consumer protection | `consumer-protection/` |
| VMI | LT | Tax | `tax-authorities/` |
| VID | LV | Tax | `tax-authorities/` |
| EMTA | EE | Tax | `tax-authorities/` |
| any authority | all | formal inquiries | `inquiries/` (privileged) |

## Response SLAs

- Routine filing/registration: per the regime's own deadline, tracked in
  the folder.
- Authority questions on file content: GC responds; response within the
  statutory period, internally targeted at 50% of it.
- Formal inquiry / investigation: `inquiries/` intake same day; counsel
  engaged within 1 business day; no employee answers an authority
  informally without GC routing.

## Correspondence convention

`YYYY-MM-DD-<authority>-<direction>-<subject>.md` (direction: in/out),
each entry noting: received/sent date, deadline, handler, status.
Originals pointer where the paper original is controlling.
