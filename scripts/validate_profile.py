"""Offline checks for the GitHub profile README (Python standard library only)."""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
readme = ROOT / "README.md"
content = readme.read_text(encoding="utf-8")
errors = []

if not content.strip():
    errors.append("README.md is empty")
if not content.startswith('<div align="center">'):
    errors.append("Expected profile header is missing")
if content.count("<div") != content.count("</div>"):
    errors.append("Unbalanced div tags")
if re.search(r"(?i)(?:ghp_[a-zA-Z0-9]{20,}|github_pat_[a-zA-Z0-9_]{20,}|-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----)", content):
    errors.append("Possible secret detected")
if re.search(r"(?i)https?://[^\\s)\\]>]+(?:token|access_token|api_key|client_secret)=", content):
    errors.append("Possible secret in URL")
links = re.findall(r"\\]\\(([^)]+)\\)", content)
for link in links:
    if not (link.startswith("https://") or link.startswith("mailto:")):
        errors.append(f"Unexpected link scheme: {link}")
if not links:
    errors.append("No Markdown links found")

if errors:
    print("Validation failed:")
    for error in errors:
        print(" -", error)
    sys.exit(1)
print(f"Validation passed: {len(links)} Markdown links, no obvious embedded secrets.")
