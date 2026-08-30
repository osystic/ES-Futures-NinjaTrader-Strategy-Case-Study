#!/usr/bin/env python3
"""Validate the OSYSTIC v2.2 sanitized public case-study boundary."""

from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "OWNERSHIP.md",
    "NOTICE.md",
    ".gitignore",
    ".env.example",
    ".editorconfig",
    "case-study.md",
    "public-showcase-manifest.json",
    ".osystic/repository.yml",
    "assets/architecture.svg",
    "assets/validation.svg",
    "docs/architecture.md",
    "docs/technical-overview.md",
    "docs/validation-methodology.md",
    "docs/results-summary.md",
    "docs/lessons-learned.md",
    "docs/disclosure-boundary.md",
    "docs/adr/README.md",
    "docs/runbook.md",
    "docs/handover.md",
    "docs/governance-exceptions.md",
    "docs/publication-record.md",
    ".github/CODEOWNERS",
    ".github/pull_request_template.md",
    ".github/ISSUE_TEMPLATE/bug_report.yml",
    ".github/ISSUE_TEMPLATE/change_request.yml",
    ".github/workflows/ci.yml",
    ".github/dependabot.yml",
]

FORBIDDEN_SUFFIXES = {
    ".cs", ".dll", ".zip", ".7z", ".rar", ".xlsx", ".xls", ".docx", ".pdf",
    ".csv", ".txt", ".xml", ".nt8", ".sqlite", ".db",
}

FORBIDDEN_NAMES = {
    "output.txt", "trades.csv", "orders.csv", "executions.csv",
}

TEXT_NAMES = {
    ".gitignore", ".env.example", ".editorconfig",
}

SECRET_PATTERNS = [
    re.compile(r"(?i)(api[_-]?key|secret|password|access[_-]?token)\s*[:=]\s*[^\s]{8,}"),
    re.compile(r"gh[pousr]_[A-Za-z0-9_]{20,}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]

IDENTITY_GUARDS = [
    re.compile(r"(?i)\bDavid\b"),
    re.compile(r"(?i)\bArslan\b"),
]


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


for relative in REQUIRED:
    if not (ROOT / relative).is_file():
        fail(f"required artifact missing: {relative}")

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue

    relative = path.relative_to(ROOT)
    lower_name = path.name.lower()

    if path.suffix.lower() in FORBIDDEN_SUFFIXES:
        fail(f"confidential/raw artifact type is not allowed: {relative}")
    if lower_name in FORBIDDEN_NAMES:
        fail(f"raw runtime artifact is not allowed: {relative}")

    is_text = path.suffix.lower() in {".md", ".json", ".py", ".yml", ".yaml", ".svg"}
    if not is_text and path.name not in TEXT_NAMES:
        continue

    text = path.read_text(encoding="utf-8", errors="strict")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            fail(f"possible secret found in {relative}")
    for pattern in IDENTITY_GUARDS:
        if pattern.search(text):
            fail(f"private identity guard triggered in {relative}")

manifest = json.loads((ROOT / "public-showcase-manifest.json").read_text(encoding="utf-8"))
if manifest.get("artifactType") != "sanitized-engineering-case-study":
    fail("unexpected public showcase manifest classification")
if manifest.get("governanceStandardVersion") != "2.2":
    fail("OSYSTIC governance version must be 2.2")
if manifest.get("publicClaims", {}).get("liveFundedDecision") != "NO-GO":
    fail("live/funded decision must remain NO-GO")
if manifest.get("publicClaims", {}).get("eligibleRegisteredCandidates") != 0:
    fail("eligible candidate count must remain zero")
if not all(manifest.get("pace", {}).get(k) for k in ("problem", "architecture", "contribution", "evidence")):
    fail("PACE publication record is incomplete")
if manifest.get("publication", {}).get("status") != "published":
    fail("publication status must remain explicit")

repository_manifest = (ROOT / ".osystic/repository.yml").read_text(encoding="utf-8")
for value in (
    'governance_standard_version: "2.2"',
    "repository_class: public-case-study",
    "visibility: public",
    "status: published",
    "live_funded_decision: NO-GO",
    "history_independent: true",
):
    if value not in repository_manifest:
        fail(f"repository governance invariant missing: {value}")

print("OSYSTIC public governance and disclosure validation: PASS")
