# platform-regulation/ — EU platform law program

Why this tree exists: **marketplaces carry obligations that generic
e-shops don't.** Hosting third-party sellers and user content makes JOL a
"platform" under DSA and a "provider of online intermediation services"
under P2B, on top of ordinary e-commerce/consumer/VAT law. Each subtree is
a regulatory instrument with: the legal memo (what the law requires), the
product spec hook (where the product implements it), and evidence pointers.

| Subtree | Instrument | Core duties |
|---------|-----------|-------------|
| `dsa/` | Reg. (EU) 2022/2065 | Trader traceability, notice-and-action, statements of reasons, complaints, transparency reports |
| `p2b/` | Reg. (EU) 2019/1150 | Terms transparency, ranking disclosure, 30-day change notice, data access |
| `gpsr/` | Reg. (EU) 2023/988 | Responsible-person rules for products sold by our sellers |
| `consumer-law/` | CRD 2011/83, Omnibus (EU) 2019/2161 | Withdrawal, review authenticity, personalized-price disclosure |
| `vat-oss/` | VAT Directive + OSS | Deemed-supplier analysis, OSS mechanics per LT/LV/EE |
| `watches/` | Horizon scanning | AI Act and upcoming instruments — one memo per instrument |

Rules:

- Memos cite the exact article and the consolidation date; national
  transposition notes carry the market tag (LT/LV/EE).
- Product spec hooks reference the implementing repo/module
  (e.g., `sellers_app` KYB, `gdpr_middleware` consent) so legal duty and
  technical control stay traceable.
- `watches/` memos end with a review date; expired reviews fail the
  quarterly GC check-in.
