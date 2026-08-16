# P2B ranking transparency — Art. 5

**Regulation (EU) 2019/1150, Art. 5 (ranking).**

## Legal position

Terms must set out the **main parameters** determining ranking, their
**relative importance**, and — where applicable — how they differ for
our own goods/services or affiliated sellers (we currently have neither;
state that explicitly rather than omitting the topic).

## Public text

The seller-facing summary lives in
`legal-texts/seller-agreement/` (§ Ranking). It must be plain-language
and kept consistent with this spec on every change (same version bump).

## Internal spec (this file)

1. **Parameter inventory** — e.g., relevance to query, seller
   performance metrics, listing completeness, recency, paid placement
   (if ever introduced — currently none; introducing it is a material
   change under Art. 5 and a P2B notice event).
2. **Relative importance** — documented weighting logic; where ML-based,
   the explanation must be maintainable (AI Act interface — see
   `watches/ai-act.md`).
3. **Differentiation statement** — no own-goods preference; documented
   and re-verified quarterly.
4. **Change control** — parameter changes require GC review + seller
   notice per `tos-change-notice.md`.

## Status

- [ ] Parameter inventory approved by product + GC
- [ ] Weighting explanation drafted
- [ ] Quarterly differentiation re-verification scheduled
