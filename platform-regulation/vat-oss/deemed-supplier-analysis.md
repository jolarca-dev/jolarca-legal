# VAT OSS — Deemed-supplier analysis

**Date:** 2026-09-02
**Status:** Position (counsel-drafted, pending GC sign-off)
**Author:** General Counsel
**Supersedes:** N/A (first position)

---

## 1. Question

Under what circumstances does Art. 14a of the VAT Directive (Directive
2006/112/EC, as amended by Directive (EU) 2019/1995 and Regulation (EU)
2019/1995) make the Journey of Life Marketplace (UAB "Journey of Life")
the **deemed supplier** for VAT purposes, such that JOL — not the actual
Seller — must account for VAT on the supply?

## 2. Legal framework

### 2.1 Art. 14a(1) — Facilitation of supplies of services

Where a taxable person (the marketplace) uses an electronic interface to
facilitate the supply of **services** by a non-established taxable
person to a customer in the EU, the marketplace is deemed to have
received and supplied the services itself.

### 2.2 Art. 14a(2) — Facilitation of goods from non-EU sellers

Where a taxable person uses an electronic interface to facilitate the
supply of **goods** from a non-established seller to a customer in the
EU, and the goods are dispatched/transported from or to a third
territory/third country in consignments of an **intrinsic value not
exceeding €150**, the marketplace is deemed to have received and
supplied the goods itself.

### 2.3 IOSS (Import One-Stop-Shop)

For goods in consignments ≤ €150 from outside the EU, the deemed
supplier may use the IOSS scheme to account for import VAT at the point
of sale rather than at import.

## 3. Application to the Marketplace

### 3.1 Baseline: intra-EU physical goods

The Marketplace's catalog consists predominantly of **physical goods
sold by EU-established sellers to EU consumers** (B2C distance sales of
funerary, memorial, religious, and sacred goods).

For this baseline scenario:

- **Art. 14a does NOT apply.** The marketplace is not the deemed
  supplier because:
  - The goods are physical (not services) — Art. 14a(1) is inapplicable;
  - The sellers are EU-established — Art. 14a(2) applies only to goods
    from non-EU sellers in consignments ≤ €150.

- **VAT treatment:** The Seller accounts for VAT at the rate applicable
  in the Member State of destination, either directly or via OSS.

### 3.2 Exception: non-EU sellers

If a seller established outside the EU lists goods on the Marketplace:

| Scenario | Deemed supplier? | VAT treatment |
|----------|-----------------|---------------|
| Non-EU seller → EU consumer, goods from outside EU, consignment ≤ €150 | **Yes** (Art. 14a(2)) | JOL is deemed supplier; IOSS recommended |
| Non-EU seller → EU consumer, goods from outside EU, consignment > €150 | **No** | Seller/importer accounts for import VAT |
| Non-EU seller → EU consumer, goods already in EU (warehoused) | **No** | Seller accounts for VAT; OSS may apply |

### 3.3 Exception: digital services

If the Marketplace ever hosts digital content (e.g., downloadable
memorial templates, digital artwork):

| Scenario | Deemed supplier? | VAT treatment |
|----------|-----------------|---------------|
| Non-EU seller → EU consumer, digital service | **Yes** (Art. 14a(1)) | JOL is deemed supplier; OSS for services |
| EU seller → EU consumer, digital service | **No** | Seller accounts for VAT via OSS |

### 3.4 Commission on marketplace fees

JOL charges Sellers a commission for Marketplace services. This is a
**separate supply** (JOL → Seller) of intermediary/electronic services:

- **B2B (Seller is a taxable person):** Reverse charge applies. JOL
  invoices without VAT; the Seller accounts for VAT under reverse
  charge in their Member State.
- **B2C (Seller is a non-taxable person):** Currently not applicable —
  all Sellers on the Marketplace are traders (taxable persons). If
  non-trader sellers are permitted, JOL's commission would be subject to
  VAT at the rate of the Seller's Member State.

## 4. Position summary

| Scenario | JOL deemed supplier? | Action |
|----------|---------------------|--------|
| EU seller → EU consumer, physical goods | **No** | Seller accounts for VAT (direct or OSS) |
| Non-EU seller → EU consumer, physical goods ≤ €150 from outside EU | **Yes** | JOL accounts for VAT; IOSS recommended |
| Non-EU seller → EU consumer, physical goods > €150 or already in EU | **No** | Seller accounts for VAT |
| Digital services from non-EU seller | **Yes** | JOL accounts for VAT via OSS |
| Commission invoicing (B2B) | N/A | Reverse charge; JOL invoices net |

## 5. Operational implications

1. **Seller onboarding:** KYB flow must capture the seller's
   establishment location. Non-EU sellers trigger deemed-supplier
   analysis before activation.
2. **Checkout logic:** For deemed-supply scenarios, the checkout must
   calculate VAT as if JOL were the supplier and route the VAT amount to
   JOL's OSS return.
3. **IOSS:** If non-EU sellers in ≤ €150 consignments are permitted,
   JOL must register for IOSS via VMI and include the IOSS number on
   customs declarations.
4. **Reporting:** JOL must maintain transaction-level records for
   deemed-supply scenarios (buyer location, goods description, value,
   dispatch origin) for OSS/IOSS returns.

## 6. Recommendation

1. **Do not actively recruit non-EU sellers** in the initial launch
   phase — the compliance burden of deemed-supply is disproportionate to
   the expected volume.
2. **If non-EU sellers are later permitted**, implement automated
   deemed-supply detection in the checkout flow before go-live.
3. **Monitor the catalog** for any goods that could be classified as
   digital content (e.g., downloadable templates) — these trigger
   Art. 14a(1) from non-EU sellers.

## 7. Review

This position will be reviewed:

- When a non-EU seller applies to list on the Marketplace;
- When the catalog expands to include digital content;
- When EU legislation amends Art. 14a or the €150 threshold;
- At least annually as part of the VAT compliance review.
