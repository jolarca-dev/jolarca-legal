# VMI (LT) — i.SAF obligation record (FR0600)

- Recorded: 2026-08-17 (STEP 26 corrections, jol-m-compliance)
- Status: obligation REGISTERED; engineering export spec pending (jol-m-data issue)
- Cross-references: `jol-m-compliance/docs/regulatory-obligations.md` OBL-001;
  `jol-m-compliance/docs/retention-schedule.md` §2 (LT 10y accounting class)

## The obligation

Lithuania's i.MAS framework requires taxpayers to submit **i.SAF** — the
digital VAT invoice register — as structured XML (**form FR0600**) covering
issued and received VAT invoices.

- **Channel:** Mano VMI, State Tax Inspectorate of the Republic of Lithuania
  (VMI); specification: vmi.lt → i.SAF (vmi.lt/evmi/i.saf)
- **Cadence:** monthly; submission **by the 20th day of the month following
  the reporting period**
- **Nil reporting:** a report is required **even when zero invoices** were
  issued/received in the period
- This is a **recurring operational filing**, not a one-time registration.

## Scope for the platform

- Lithuanian entity invoicing (marketplace commission invoices, seller
  invoicing flows) — Lithuanian pilot scope first; LV/EE analogues
  `[COUNSEL-TO-CONFIRM]`.
- Source of truth for the export: finance marts in jol-m-data (`fct_vat_oss`,
  invoice models) — tracked in jol-m-data issue "i.SAF FR0600 export".

## Penalties

Penalties for non-filing/late filing: `[COUNSEL-TO-CONFIRM]` — amounts not
verified against the primary source; do not quote.

## Open items for tax advisor

1. Confirm FR0600 schema version currently in force and any i.SAF-T
   distinctions applicable to our taxpayer class `[COUNSEL-TO-CONFIRM]`
2. Confirm penalty regime for late/missing nil reports `[COUNSEL-TO-CONFIRM]`
3. Confirm whether marketplace commission invoices require line-level seller
   identifiers in the register `[COUNSEL-TO-CONFIRM]`
