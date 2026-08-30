# Security and Responsible Disclosure

This public repository contains sanitized case-study documentation only.

## Reporting

Do not publish suspected credentials, private data, client identity or confidential source in an issue. Use GitHub private vulnerability reporting if available, or contact OSYSTIC through an approved private company channel.

## Repository security boundary

The repository must not contain:

- NinjaScript/C# client implementation;
- private keys, tokens, credentials or local `.env` files;
- raw NT8 logs, XML/CSV/TXT exports or screenshots with identifiers;
- client conversations, names, contact details or commercial information;
- private market/news data;
- delivery archives, private artifact hashes or private repository links.

CI checks required artifacts, forbidden extensions, likely secret patterns, identity guards and approved result invariants.

## Dependency policy

Dependabot reviews GitHub Actions references. Updates must pass the normal PR validation and are not blanket auto-merged.

## Performance safety

No material in this repository is trading advice, a guarantee or approval for live/funded use. A security or factual correction must not weaken that boundary.
