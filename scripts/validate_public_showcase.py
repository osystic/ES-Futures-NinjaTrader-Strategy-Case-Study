#!/usr/bin/env python3
"""Validate the sanitized public case-study boundary."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "case-study.md",
    "NOTICE.md",
    "public-showcase-manifest.json",
    "assets/architecture.svg",
    "assets/validation.svg",
    "docs/technical-overview.md",
    "docs/validation-methodology.md",
    "docs/results-summary.md",
    "docs/lessons-learned.md",
    "docs/disclosure-boundary.md",
]

FORBIDDEN_SUFFIXES = {
    ".cs", ".dll", ".zip", ".7z", ".rar", ".xlsx", ".xls",
    ".csv", ".txt", ".xml", ".nt8", ".sqlite", ".db",
}

FORBIDDEN_NAMES = {
    "output.txt", "trades.csv", "orders.csv", "executions.csv",
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

    if path.suffix.lower() not in {".md", ".json", ".py", ".yml", ".yaml", ".svg"}:
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
if manifest.get("publicClaims", {}).get("liveFundedDecision") != "NO-GO":
    fail("live/funded decision must remain NO-GO")
if manifest.get("publicClaims", {}).get("eligibleRegisteredCandidates") != 0:
    fail("eligible candidate count must remain zero")

print("Public showcase validation: PASS")
