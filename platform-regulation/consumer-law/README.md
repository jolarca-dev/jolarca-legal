# Consumer law — CRD 2011/83 + Omnibus (EU) 2019/2161

Marketplace-specific consumer-law obligations beyond the buyer-terms text.

## Omnibus duties that bind the marketplace directly

1. **Review authenticity (Art. 7 amending UCPD):** if we display reviews,
   we must disclose whether and how we ensure they come from actual
   purchasers. Spec: verified-purchase flag mechanics in product; the
   disclosure text lives in `legal-texts/community-standards/` § Reviews.
   Displaying unverified reviews without saying so is a misleading
   practice — do not display review counts before verification logic
   exists.
2. **Personalized pricing (Art. 6 CRD insertion):** if any automated
   price adjustment per user exists, disclosure is mandatory. Current
   posture: **no personalized pricing**; this memo re-checks quarterly
   (ties to `watches/ai-act.md` when ML pricing appears).
3. **Marketplace parameter disclosure (Art. 6a CRD):** who is the seller
   (trader or not), applicability of consumer rights, division of
   obligations between marketplace and seller — implemented via the
   listing-page information block (spec with product).
4. **Discounts with reference prices (Art. 6a UCPD):** lowest-price-
   30-days rule for price-reduction announcements — listing rules in
   `legal-texts/community-standards/` + enforcement in moderation.

## CRD core (implemented in buyer-terms)

14-day withdrawal, pre-contract information (Art. 6), delivery rules,
payment button labeling ("order with obligation to pay" equivalents
LT/LV/EE).

## Status

- [ ] Review-authenticity disclosure shipped with verification feature
- [ ] Art. 6a listing-page block spec agreed
- [ ] Discount-display rules approved
