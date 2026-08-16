# GPSR — General Product Safety Regulation (EU) 2023/988

Applies from 13 December 2024; replaces the General Product Safety
Directive for our product categories.

## Why it matters for a marketplace

- **Responsible person rule (Art. 4/16):** products placed on the EU
  market need an EU-established responsible person. Our sellers are
  usually EU-established (Baltics-first), but the marketplace must
  surface that information and act when it is missing.
- **Marketplace duties (Art. 22):** single safety gateway/contact point,
  cooperation with Safety Gate / RAPEX, proactive takedown duties on
  notified dangerous products, information to buyers on recalls affecting
  products they purchased (where identifiable).
- **Listing requirements:** safety information, warnings, and
  responsible-person details must appear in the offer.

## Product spec hooks

1. Onboarding: responsible-person capture for non-EU sellers (ties to
   KYB in `dsa/trader-traceability.md`).
2. Listing schema: safety warnings field per category (sacred goods with
   candles/incense = fire-safety labeling hooks).
3. Safety Gate feed: monitoring process + takedown SOP.
4. Recall notification to past buyers: channel + data-minimization note
   (GDPR boundary — with DPO via jol-m-compliance).

## Status

- [ ] Category risk map (which of our goods carry GPSR exposure)
- [ ] Safety Gate monitoring SOP
- [ ] Recall-to-buyer notification flow with DPO sign-off
