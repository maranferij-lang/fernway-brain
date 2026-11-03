#!/usr/bin/env python3
"""Checks for the Fernway brain.

Default mode (runs in CI on every pull request):
  1. Every content doc has front matter with owner, source and last_verified.
  2. No tracked text file contains emails, phone numbers, key-like strings
     or password-style assignments.
  Exits 1 if anything fails.

--stale DAYS: prints a Markdown list of docs whose last_verified is older
than DAYS (used by the monthly review workflow). Always exits 0.

Standard library only, so it runs anywhere python3 does.
"""

import argparse
import datetime as dt
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# Repo machinery, not company facts: no front matter required.
FRONT_MATTER_EXEMPT = {"README.md", "CLAUDE.md", "CONTRIBUTING.md"}
REQUIRED_KEYS = ("owner", "source", "last_verified")

# This file holds the patterns themselves, so it is not scanned.
SCAN_EXEMPT = {"scripts/check_docs.py"}
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".txt", ".json", ".toml", ""}

SENSITIVE_PATTERNS = [
    ("email address", re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[A-Za-z]{2,}")),
    ("phone number", re.compile(r"(?<![\w.])(?:\+|00|\(0|0)\d[\d\s().-]{7,}\d")),
    ("Anthropic/OpenAI-style key", re.compile(r"\bsk-[A-Za-z0-9_-]{16,}")),
    ("GitHub token", re.compile(r"\b(?:ghp|gho|ghu|ghs|ghr)_[A-Za-z0-9]{20,}|\bgithub_pat_[A-Za-z0-9_]{20,}")),
    ("AWS access key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("Slack token", re.compile(r"\bxox[abposr]-[A-Za-z0-9-]{10,}")),
    ("Stripe key", re.compile(r"\b(?:sk|pk|rk)_(?:live|test)_[A-Za-z0-9]{10,}")),
    ("private key block", re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----")),
    ("JWT", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}")),
    ("long random string", re.compile(r"(?<![A-Za-z0-9/_.-])[A-Za-z0-9+/_-]{40,}={0,2}(?![A-Za-z0-9/_.-])")),
    ("password-style assignment", re.compile(
        r"(?i)\b(?:password|passwd|pwd|passcode|secret|token|api[_-]?key|login|credentials?)\b\s*[:=]\s*"
        r"(?!\$\{\{)['\"]?[^\s'\"]{4,}")),
]


def tracked_files():
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        return [ROOT / line for line in out.splitlines() if line]
    except (subprocess.CalledProcessError, FileNotFoundError):
        return [p for p in ROOT.rglob("*") if p.is_file() and ".git" not in p.parts]


def rel(path):
    return path.relative_to(ROOT).as_posix()


def needs_front_matter(path):
    r = rel(path)
    return path.suffix == ".md" and r not in FRONT_MATTER_EXEMPT and not r.startswith(".github/")


def read_front_matter(text):
    if not text.startswith("---\n"):
        return None
    end = text.find("\n---", 4)
    if end == -1:
        return None
    fields = {}
    for line in text[4:end].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            fields[key.strip()] = value.strip().strip("'\"")
    return fields


def check_front_matter(path, today):
    fields = read_front_matter(path.read_text(encoding="utf-8"))
    if fields is None:
        return ["no front matter (needs owner, source, last_verified)"]
    errors = [f"missing or empty '{k}'" for k in REQUIRED_KEYS if not fields.get(k)]
    if fields.get("source") and not re.search(r"pack §\d", fields["source"]):
        errors.append("'source' must cite a pack section, e.g. 'pack §4 (How things actually work)'")
    if fields.get("last_verified"):
        try:
            verified = dt.date.fromisoformat(fields["last_verified"])
            if verified > today:
                errors.append(f"'last_verified' {verified} is in the future")
        except ValueError:
            errors.append("'last_verified' must be YYYY-MM-DD")
    return errors


def scan(path):
    hits = []
    for n, line in enumerate(path.read_text(encoding="utf-8", errors="replace").splitlines(), 1):
        for label, pattern in SENSITIVE_PATTERNS:
            if label == "phone number":
                for m in pattern.finditer(line):
                    if len(re.sub(r"\D", "", m.group())) >= 9:
                        hits.append((n, label))
                        break
            elif pattern.search(line):
                hits.append((n, label))
    # Never echo the matched text: if it is a real secret, CI logs are public.
    return hits


def run_checks():
    today = dt.date.today()
    failures = 0
    for path in tracked_files():
        if not path.exists():
            continue
        r = rel(path)
        if needs_front_matter(path):
            for err in check_front_matter(path, today):
                print(f"FRONT MATTER  {r}: {err}")
                failures += 1
        if r not in SCAN_EXEMPT and path.suffix in TEXT_SUFFIXES:
            for line, label in scan(path):
                print(f"SENSITIVE     {r}:{line}: looks like: {label} (value not shown)")
                failures += 1
    if failures:
        print(f"\n{failures} problem(s). See CONTRIBUTING.md, 'Hard rules' and 'Excluded on purpose'.")
        return 1
    print("check_docs: all good.")
    return 0


def report_stale(days):
    cutoff = dt.date.today() - dt.timedelta(days=days)
    stale = []
    for path in tracked_files():
        if not path.exists() or not needs_front_matter(path):
            continue
        fields = read_front_matter(path.read_text(encoding="utf-8")) or {}
        try:
            verified = dt.date.fromisoformat(fields.get("last_verified", ""))
        except ValueError:
            verified = None
        if verified is None or verified < cutoff:
            stale.append((rel(path), fields.get("owner") or "no owner", verified or "never"))
    if stale:
        print(f"Docs not verified in the last {days} days:\n")
        for r, owner, verified in sorted(stale):
            print(f"- [ ] `{r}` (owner: {owner}, last verified: {verified})")
    else:
        print(f"Every doc was verified in the last {days} days.")
    return 0


def main():
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--stale", type=int, metavar="DAYS", help="list docs not verified in DAYS days")
    args = parser.parse_args()
    return report_stale(args.stale) if args.stale is not None else run_checks()


if __name__ == "__main__":
    sys.exit(main())
