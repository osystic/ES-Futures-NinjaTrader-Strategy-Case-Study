# Public Showcase Runbook

## Purpose

This runbook governs maintenance, validation, correction and withdrawal of the sanitized public case study.

## Change workflow

1. Open an issue with the requested outcome, acceptance criteria and evidence source.
2. Use a short issue-linked branch.
3. Open a draft PR.
4. Update related PACE, results, disclosure and publication records together.
5. Run `python scripts/validate_public_showcase.py`.
6. Confirm no protected source/data/identity or unsupported claim is present.
7. Squash merge after review and close the issue.

## Claim update

A public metric or outcome may change only when:

- the private evidence source is identified;
- the calculation and wording are reviewed;
- confidentiality/IP restrictions remain satisfied;
- founder approval is recorded for the new artifact version and channels.

Do not infer positive outcomes from client acceptance, payment, technical functionality or isolated historical windows.

## Incident or disclosure failure

If confidential material or an unsupported claim is discovered:

1. preserve incident evidence privately;
2. notify Shawaiz Arif;
3. remove public exposure through an approved correction/withdrawal action;
4. rotate any exposed credential immediately;
5. assess Git history and forks before declaring containment;
6. document the correction and preventive control.

## Rollback and withdrawal

Revert to the last approved public commit through a reviewed PR where possible. If continued publication is unsafe, the founder may withdraw/archive the case study. Do not rewrite history without an approved incident plan.

## Operational boundary

There is no deployable trading system or public runtime in this repository. CI validates documentation integrity and disclosure safety only.
