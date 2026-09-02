# VAT OSS — Registration mechanics per market

**Date:** 2026-09-02
**Status:** Position (counsel-drafted, pending GC sign-off)
**Author:** General Counsel
**Supersedes:** N/A (first position)

---

## 1. Overview

The One-Stop-Shop (OSS) is an EU VAT simplification mechanism that
allows a taxable person to account for VAT on cross-border B2C distance
sales of goods and services through a single registration in one Member
State, rather than registering in every destination Member State.

This memo sets out JOL's OSS registration obligations and the
obligations of Sellers on the Marketplace.

## 2. Legal basis

- Directive 2006/112/EC (VAT Directive), Title V, Chapter 6 (OSS
  scheme), as amended by Directive (EU) 2017/2455 and (EU) 2019/1995.
- Council Implementing Regulation (EU) 2019/2026 (implementing
  measures).
- National transpositions: LT (VMI), LV (VID), EE (EMTA).

## 3. OSS schemes

### 3.1 Union OSS (goods and services)

Applies to:
- Intra-EU B2C distance sales of goods (Art. 33–34 VAT Directive);
- B2C supplies of services where the place of supply is the Member State
  of the supplier (Art. 58 VAT Directive).

**Registration:** The taxable person registers for OSS in the Member
State of establishment (or identification). JOL's OSS registration is
via **VMI (Lithuania)**.

### 3.2 Non-Union OSS (services only)

Applies to non-EU taxable persons making B2C supplies of
telecommunications, broadcasting, or electronic services to EU
consumers. Not applicable to JOL (EU-established).

### 3.3 Import OSS (IOSS)

Applies to distance sales of goods imported from third territories in
consignments ≤ €150. JOL may need IOSS registration if it becomes a
deemed supplier under Art. 14a (see `deemed-supplier-analysis.md`).

## 4. JOL's OSS obligations

### 4.1 When does JOL need OSS?

| Scenario | JOL OSS required? | Notes |
|----------|-------------------|-------|
| JOL sells its own goods B2C cross-border | **Yes** | JOL is the supplier; OSS via VMI |
| JOL is deemed supplier (Art. 14a) | **Yes** | See deemed-supplier analysis |
| JOL provides commission services to Sellers | **No** (reverse charge) | Commission invoicing is B2B |
| JOL facilitates Seller's B2C sales (not deemed supplier) | **No** (Seller's obligation) | Seller accounts for own VAT |

### 4.2 JOL's OSS registration

| Field | Value |
|-------|-------|
| OSS scheme | Union OSS |
| Member State of identification | Lithuania (VMI) |
| OSS registration number | LT[OSS number — to be assigned] |
| Effective date | [To be set upon registration] |
| Quarterly return deadline | End of month following the quarter |

### 4.3 OSS return obligations

JOL must file an OSS return for each calendar quarter in which it makes
qualifying supplies. The return must include:

- Member State of consumption;
- VAT rate applied;
- Taxable amount;
- VAT amount due;
- Any amendments to prior returns.

**Deadline:** By the end of the month following the quarter (e.g.,
Q1 return due by 30 April).

**Payment:** VAT due is paid to VMI, which distributes to the
destination Member States.

## 5. Sellers' OSS obligations

### 5.1 EU-established Sellers

Each Seller is independently responsible for its own VAT obligations:

| Seller scenario | VAT treatment |
|-----------------|---------------|
| LT Seller → LT Buyer | LT VAT at LT rate; domestic supply |
| LT Seller → LV/EE Buyer | LT Seller uses OSS (via VMI) or registers directly in destination MS |
| LV Seller → LT Buyer | LV Seller uses OSS (via VID) or registers directly in LT |
| EE Seller → LT/LV Buyer | EE Seller uses OSS (via EMTA) or registers directly |

### 5.2 Marketplace's role in Seller VAT

The Marketplace must provide Sellers with the data needed for their own
VAT compliance:

| Data point | Provided by Marketplace? | Format |
|------------|-------------------------|--------|
| Buyer's Member State | Yes | Per-transaction report |
| Total sale price (incl. VAT) | Yes | Per-transaction |
| VAT amount collected | Yes | Per-transaction, per rate |
| Delivery confirmation | Yes | Carrier data |
| Refund/credit note data | Yes | Per-transaction |

### 5.3 Sellers below the €10,000 threshold

Sellers whose cross-border B2C distance sales (across all platforms and
own channels) do not exceed €10,000 per year may apply the VAT rate of
their own Member State (Art. 284 VAT Directive) rather than the
destination Member State rate. The Marketplace should display a note to
Sellers about this threshold but is not responsible for monitoring it.

## 6. Per-market registration requirements

### 6.1 Lithuania (VMI)

| Requirement | Details |
|-------------|---------|
| VAT registration | Required for domestic supplies and as OSS Member State of identification |
| OSS registration | Via VMI portal |
| i.SAF / i.VAZ | Electronic invoicing system (i.SAF for sales, i.VAZ for purchases) — mandatory for LT VAT payers |
| SAFT | Standard Audit File for Tax — must be provided on request |

### 6.2 Latvia (VID)

| Requirement | Details |
|-------------|---------|
| VAT registration | Required if JOL has a fixed establishment in LV or makes domestic LV supplies |
| OSS | Via VMI (LT) as Member State of identification; no separate LV OSS registration needed |
| Local obligations | None unless JOL has a fixed establishment |

### 6.3 Estonia (EMTA)

| Requirement | Details |
|-------------|---------|
| VAT registration | Required if JOL has a fixed establishment in EE or makes domestic EE supplies |
| OSS | Via VMI (LT) as Member State of identification; no separate EE OSS registration needed |
| Local obligations | None unless JOL has a fixed establishment |

## 7. Commission invoicing — VAT treatment

JOL's commission to Sellers is a supply of **intermediary services**
(electronic marketplace services):

| Seller type | VAT treatment of commission |
|-------------|---------------------------|
| EU taxable person (B2B) | Place of supply = Seller's Member State (Art. 44 VAT Directive). Reverse charge applies. JOL invoices without VAT. |
| Non-EU taxable person | Place of supply = where the customer is established. Reverse charge or local rules apply. |
| Non-taxable person (B2C) | Not currently applicable — all Sellers are traders. If permitted, VAT at the rate of the Seller's MS. |

**Invoice requirements:**
- JOL's invoice must show: JOL's VAT ID, Seller's VAT ID (where
  available), description of services, amount, "reverse charge" notation
  where applicable.
- Prices in invoices are exclusive of VAT (CL-51).

## 8. Distance-sale evidence

For OSS purposes, JOL must maintain evidence of the buyer's location
(Member State). Acceptable evidence includes:

- Buyer's self-declared address at registration;
- IP address geolocation (as corroborating evidence);
- Delivery address (most reliable for goods);
- Payment method issuing bank location (as corroborating evidence).

**Two non-contradictory pieces of evidence** are required for each
transaction. Where evidence is contradictory, the more reliable piece
prevails (delivery address > IP address).

## 9. Review

This position will be reviewed:

- Upon JOL's OSS registration with VMI;
- When JOL expands to sell its own goods;
- When EU legislation amends the OSS scheme;
- At least annually as part of the VAT compliance review.
