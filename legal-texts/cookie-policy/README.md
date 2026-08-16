# cookie-policy/ — Cookies, consent banner, and the enforcement contract

This text is paired with a technical contract: the consent-banner
specification here defines what the marketplace `gdpr_middleware`
enforces server-side. Text and middleware must stay in lockstep —
a change to banner behavior is a change to this text.

- No non-essential storage before affirmative consent; rejection as easy
  as acceptance (no dark patterns — EDPB guidance).
- Consent records (what version, when, what options) are kept per
  `jol-m-compliance/lawful-basis/`; version changes here can invalidate
  prior consent (cross-check script).

Section skeleton (en): 1. what cookies/storage we use · 2. categories
(essential / analytics / marketing) with per-cookie table ·
3. consent mechanics & how to withdraw · 4. banner contract summary ·
5. third-party SDKs (payments, delivery, analytics) · 6. changes.
