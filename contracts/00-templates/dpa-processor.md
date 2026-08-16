# Template: DPA — JOL as processor (rare)

<!-- TEMPLATE STATUS: scaffold — counsel completes wording before first use.
     Usage: institutional diocese-type arrangements where the counterparty
     is controller and JOL processes on their instructions. Confirm role
     analysis BEFORE drafting — most marketplace flows make JOL controller
     or independent controller; processor role is the exception. -->

## Gate

- [ ] Role analysis memo filed in `opinions/` (controller vs processor)
- [ ] GC approval to act as processor recorded
- [ ] Sub-processing chain acceptable (JOL's own processors listed)

## Deal-sheet defaults

| Parameter | Default | Concession limit |
|-----------|---------|------------------|
| Instructions | documented, written only | no verbal instruction channels |
| Breach notice to controller | ≤ 72 hours | no shorter than our own detection capability |
| Audit by controller | annual, 30-day notice, reasonable scope | no unrestricted access to other clients' data |
| Liability | GDPR Art. 82 framework; caps per CL-01 w/ CL-02 carve-outs | |

## Structure

Mirror of `dpa-controller-processor.md` with roles swapped:
1. Parties & roles (counterparty controller, JOL processor)
2. Documented instructions
3. Confidentiality
4. Security measures (our TOMs annex — reuse ISO/SOC evidence)
5. Sub-processor mechanics (our standard list)
6. Data subject rights assistance
7. Breach notification & cooperation
8. Audit rights
9. Transfers
10. End-of-service return/destruction
11. Liability
12. Annexes

## Watch items

- Processor role limits what the marketplace product may do with the data —
  product must be able to honor instruction-only processing for the tenant.
- Joint-controller is usually the better fit for marketplace features;
  do not accept processor role by default.
