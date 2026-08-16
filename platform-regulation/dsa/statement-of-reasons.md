# DSA statement of reasons — Art. 17 moderation decision notices

**Regulation (EU) 2022/2065, Art. 17 (statement of reasons).**

## Legal position

Every restriction we impose (removal, demotion, demonetization, account
suspension, KYB-driven restriction) must carry a statement of reasons
containing: whether the measure involves automated means, the facts
relied upon, the ground relied on (illegality vs. contractual
incompatibility, with the specific provision cited), redress options
(internal complaint Art. 20, out-of-court settlement Art. 21, courts).

## Template elements (decision notice)

1. Measure taken + scope + effective time.
2. Automated involvement: yes/no + human review performed.
3. Factual basis (as far as compatible with ongoing review).
4. Ground: illegal content → legal provision; incompatible content →
   clause of `legal-texts/community-standards/` (cite section number —
   this is why that text must stay quotable).
5. Redress ladder with links/deadlines.
6. Art. 24(5) transparency-database submission where the measure targets
   illegal content (VLOU duty does not apply to us; keep the data anyway
   for reporting hygiene).

## Product spec hook

Moderation tooling renders the statement from structured decision fields;
free-text-only decisions are rejected by tooling.

## Status

- [ ] Decision-field schema agreed with product
- [ ] Clause citation map (standards section ↔ offense categories)
