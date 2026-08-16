# Template: Contractor agreement (dev/design)

<!-- TEMPLATE STATUS: scaffold — counsel completes wording before first use.
     Usage: independent contractors delivering dev/design work product.
     IP assignment and confidentiality are the load-bearing clauses. -->

## Deal-sheet defaults

| Parameter | Default | Concession limit |
|-----------|---------|------------------|
| IP | full assignment on creation (CL-40); background IP license-only (CL-41) | no-concede on assignment of deliverables |
| Moral rights | waived to extent permitted | |
| Open source | prior written approval for copyleft deps (see license-compliance) | AGPL in product requires GC+eng sign-off |
| Confidentiality | JOL unilateral or mutual NDA incorporated | |
| Non-solicitation | 12 months, mutual | |
| Status | independent contractor; no employment representation | LT-specific: check misclassification risk |

## Structure

1. Parties, engagement, statement-of-work mechanism
2. Deliverables & acceptance
3. Fees, expenses, invoicing (Net-30 per CL-50)
4. IP assignment (CL-40) + background IP (CL-41) + open-source compliance
5. Confidentiality + return of materials
6. Data protection (contractor NDA/DPA if accessing personal data)
7. Warranties: originality, non-infringement
8. Term & termination (30-day notice; CL-31)
9. Independent contractor status; taxes on contractor
10. Governing law (CL-10), notices

## Linkages

- Executed agreements file under `contracts/employment/` (access-restricted).
- OSS contributions by contractors need CLA/DCO handling per
  `intellectual-property/copyright/`.
