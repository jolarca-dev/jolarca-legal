# VAT OSS — Per-country VAT rate table

**Date:** 2026-09-02
**Status:** Reference (updated as rates change)
**Source:** EU Commission VAT rates database; national legislation
**Last verified:** 2026-09-02

---

## 1. Standard rates

| Member State | Standard rate | Authority | Legal reference |
|-------------|--------------|-----------|-----------------|
| **Lithuania (LT)** | 21% | VMI | Law on VAT of the Republic of Lithuania, Art. 2 |
| **Latvia (LV)** | 21% | VID | Latvian VAT Law (Pievienotās vērtības nodokļa likums), Art. 3 |
| **Estonia (EE)** | 22% | EMTA | Estonian VAT Act (käibemaksuseadus), § 15 (rate increased from 20% to 22% effective 1 January 2025) |

## 2. Reduced rates relevant to the Marketplace catalog

The Marketplace sells funerary, memorial, religious, and sacred goods.
The following reduced rates may apply depending on the goods category:

### 2.1 Lithuania

| Category | Rate | Conditions | Legal reference |
|----------|------|------------|-----------------|
| Standard goods | 21% | Default | Art. 2 Law on VAT |
| Books, printed matter | 9% | Including religious texts | Annex IX, List I |
| Funeral services | 9% | Services only; goods at standard rate unless specifically listed | Annex IX |
| Religious items | 21% | No specific reduced rate for religious goods in LT | — |

### 2.2 Latvia

| Category | Rate | Conditions | Legal reference |
|----------|------|------------|-----------------|
| Standard goods | 21% | Default | Art. 3 VAT Law |
| Books, printed matter | 5% | Including religious texts | Annex I |
| Funeral services | 12% | Services; goods may be at standard rate | Annex I |
| Religious items | 21% | No specific reduced rate | — |

### 2.3 Estonia

| Category | Rate | Conditions | Legal reference |
|----------|------|------------|-----------------|
| Standard goods | 22% | Default (from 1 Jan 2025) | § 15 VAT Act |
| Books, printed matter | 9% | Including religious texts | § 15(3) |
| Funeral services | 9% | Services; goods at standard rate | § 15(3) |
| Religious items | 22% | No specific reduced rate | — |

## 3. Application to Marketplace goods

### 3.1 General rule

Most goods on the Marketplace (funerary monuments, memorial items,
religious objects, sacred goods, candles, incense, etc.) are **physical
goods** subject to the **standard rate** of the destination Member State.

### 3.2 Exceptions

| Goods type | LT | LV | EE | Notes |
|-----------|----|----|----|-------|
| Printed religious texts (books, prayer books) | 9% | 5% | 9% | Reduced rate for books/printed matter |
| Funeral services (if offered) | 9% | 12% | 9% | Services only; physical goods at standard rate |
| Memorial candles (standard) | 21% | 21% | 22% | Physical goods; standard rate |
| Engraved memorial items | 21% | 21% | 22% | Custom goods; standard rate |
| Religious artwork (physical) | 21% | 21% | 22% | Physical goods; standard rate |
| Digital content (if offered) | 21% | 21% | 22% | Electronically supplied services; standard rate |

### 3.3 Cross-border B2C — which rate applies?

For distance sales of goods to consumers in another Member State:

- **The VAT rate of the destination Member State applies** (where the
  goods are delivered to the consumer).
- Example: A Lithuanian seller ships a memorial candle to a consumer in
  Latvia → Latvian VAT at 21% applies.
- Example: A Latvian seller ships a prayer book to a consumer in
  Estonia → Estonian VAT at 9% (reduced rate for books) applies.

## 4. Rate comparison table (Marketplace-relevant)

| Goods category | LT rate | LV rate | EE rate | Notes |
|---------------|---------|---------|---------|-------|
| Physical goods (general) | 21% | 21% | 22% | Standard rate |
| Books / printed matter | 9% | 5% | 9% | Reduced rate |
| Funeral services | 9% | 12% | 9% | Services only |
| Digital services | 21% | 21% | 22% | Standard rate |
| Commission (JOL → Seller) | Reverse charge | Reverse charge | Reverse charge | B2B intermediary service |

## 5. Checkout implementation requirements

The Marketplace checkout must:

1. Determine the destination Member State (from delivery address);
2. Look up the applicable VAT rate for the goods category and
   destination MS;
3. Display the total price inclusive of VAT;
4. Show the VAT amount and rate on the order confirmation;
5. Report the VAT amount per MS and rate for the Seller's OSS return
   (or for JOL's OSS return if JOL is the deemed supplier).

## 6. Review schedule

VAT rates change periodically. This table must be reviewed:

- When any Member State announces a rate change;
- At least annually (January review before any 1 January changes);
- When new goods categories are added to the Marketplace catalog.

**Next scheduled review:** January 2027.
