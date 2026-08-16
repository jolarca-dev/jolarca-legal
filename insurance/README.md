# insurance/ — Coverage strategy & claims

## Strategy

The program must cover the exposures a marketplace actually carries:
data breach (GDPR fines are uninsurable in some jurisdictions — the
value is breach response), platform liability for moderation/contract
disputes, directors' exposure, professional negligence, and general
liability.

| Line | Covers | Key ties |
|------|--------|----------|
| `cyber/` | Breach response, business interruption, extortion | SECURITY.md incident flow; breach coach first-call |
| `d-and-o/` | Directors & officers decisions | corporate/board actions |
| `professional-liability/` | Errors & omissions in services | customer/partner disputes |
| `general-liability/` | Bodily injury/property damage (events, offices) | — |
| `claims/` | Claims register + correspondence | disputes/ linkage |

## Claims procedure

1. Potential claim identified (incl. at dispute intake) → **notify insurer
   within the policy window** — late notice can void coverage; this check
   is mandatory at `disputes/` intake.
2. Claim file opened in `claims/` with policy reference, notice date,
   adjuster/counsel assignment.
3. Counsel coordination: insurer's panel firm vs. retained counsel per
   policy terms.
4. Reservation-of-rights letters get GC review the day they arrive.

Policies themselves (wording PDFs) live in DMS custody; here we keep the
schedule summary + contacts per line.
