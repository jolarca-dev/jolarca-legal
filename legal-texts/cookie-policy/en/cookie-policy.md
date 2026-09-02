---
text: cookie-policy
language: en
version: 1.0.0
status: approved
effective_date: ""
approved_by: "general-counsel"
supersedes: ""
---

# Cookie Policy — Journey of Life Marketplace

**Effective date:** [to be set upon publication]
**Last updated:** [to be set upon publication]

This Cookie Policy explains how JOL uses cookies and similar storage
technologies (local storage, session storage) on the Marketplace. It is
paired with the consent-banner specification enforced by the
Marketplace's GDPR middleware.

## 1. What we store and why

We use cookies and similar technologies in four categories:

| Category | Purpose | Consent required? |
|----------|---------|-------------------|
| **Essential** | Core Marketplace functionality (session, security, CSRF, cart) | No — strictly necessary |
| **Functional** | User preferences (language, currency, accessibility) | No — strictly necessary |
| **Analytics** | Understanding usage patterns to improve the Marketplace | Yes |
| **Marketing** | Targeted communications (only with explicit consent) | Yes |

## 2. Category table

### 2.1 Essential cookies (no consent required)

| Name | Provider | Purpose | Duration |
|------|----------|---------|----------|
| `sessionid` | JOL | Server-side session identifier | Session |
| `csrftoken` | JOL | Cross-site request forgery protection | 1 year |
| `cart` | JOL | Shopping cart state | Session |
| `consent` | JOL | Stores the user's cookie consent choices | 24 months |

### 2.2 Functional cookies (no consent required)

| Name | Provider | Purpose | Duration |
|------|----------|---------|----------|
| `language` | JOL | Preferred display language (lt/lv/et/en) | 12 months |
| `currency` | JOL | Preferred currency display | 12 months |

### 2.3 Analytics cookies (consent required)

| Name | Provider | Purpose | Duration | Third-party transfer |
|------|----------|---------|----------|----------------------|
| `_ga` | Google Analytics (GA4) | Unique visitor identification | 24 months | Yes (Google LLC, US) |
| `_gid` | Google Analytics (GA4) | Session tracking | 24 hours | Yes (Google LLC, US) |
| Plausible Analytics | Self-hosted / EU | Privacy-friendly usage analytics | None (no persistent cookies) | No |

### 2.4 Marketing cookies (consent required)

_No marketing cookies are deployed at this time. If introduced, they
will be listed here with the same level of detail, and the consent
banner will be updated before deployment._

## 3. Your choices

### 3.1 Consent banner

On your first visit to the Marketplace, a consent banner is displayed
allowing you to:

- **Accept all** non-essential cookies;
- **Reject all** non-essential cookies (equal prominence to "Accept");
- **Customise** your choices per category using individual toggles.

The banner remains visible until you make an active choice. Continued
browsing without interacting with the banner does **not** constitute
consent.

### 3.2 Changing your preferences

You can change or withdraw your consent at any time:

- **In-app:** Via the "Cookie Settings" link in the page footer.
- **Browser:** Via your browser's cookie management settings.

Withdrawal of consent is as easy as giving it — the same interface and
the same number of clicks.

### 3.3 Browser "Do Not Track"

The Marketplace respects the Global Privacy Control (GPC) signal where
detected. However, because DNT/GPC signals are not yet uniformly
recognised, we recommend using the in-app consent controls for
reliable preference management.

## 4. The consent contract (banner specification)

This section defines the normative requirements enforced server-side by
the Marketplace's GDPR middleware. The banner implementation must
satisfy all of the following:

### 4.1 Pre-consent enforcement

- **No non-essential cookies or local storage** may be set before the
  user has given affirmative consent. This is enforced server-side: the
  middleware strips non-essential `Set-Cookie` headers from responses
  sent to users without a valid consent record.
- The consent record must include: the consent version, timestamp,
  categories accepted, and categories rejected.

### 4.2 Equal prominence

- The "Reject" or "Reject all" option must be displayed with equal
  visual prominence (same size, colour, position) as the "Accept" or
  "Accept all" option.
- Dark patterns (pre-ticked boxes, colour asymmetry, nagging) are
  prohibited.

### 4.3 Re-prompt cadence

- The consent banner is re-displayed only when:
  - The user has not yet made a choice;
  - The cookie categories have changed materially (new cookie added);
  - The consent version has expired (after 24 months).
- Users who have rejected all non-essential cookies are **not**
  re-prompted more frequently than every 6 months.

### 4.4 Consent withdrawal

- Withdrawal must be achievable in the same number of clicks as initial
  consent (maximum 2 clicks from any page).
- Upon withdrawal, all non-essential cookies set prior to withdrawal are
  deleted immediately.

### 4.5 Consent record

- Each consent event is recorded with: consent version ID, timestamp,
  user identifier (session or account), categories accepted/rejected,
  and the interface version displayed.
- Consent records are retained for 24 months.

## 5. Third-party SDKs

The Marketplace integrates the following third-party services that may
set cookies or similar technologies:

| Service | Provider | Cookies set | Purpose | Privacy policy |
|---------|----------|-------------|---------|----------------|
| Stripe Elements | Stripe Payments Europe Ltd. | `__stripe_mid`, `__stripe_sid` | Payment fraud detection | stripe.com/privacy |
| Google Analytics | Google LLC | `_ga`, `_gid` | Usage analytics (only with consent) | policies.google.com/privacy |

All third-party cookies are blocked by the middleware until the user
consents to the relevant category. Third-party providers' own privacy
policies govern their processing of data collected via their cookies.

## 6. Changes

We may update this Cookie Policy when we add or remove cookies, change
cookie purposes, or update the consent mechanism.

- **New cookie or category:** The consent banner is re-displayed to all
  users who previously consented.
- **Removal of a cookie:** No re-consent required.
- **Purpose change:** Treated as a new cookie; consent re-obtained.

All versions are archived and available from the DPO on request.
