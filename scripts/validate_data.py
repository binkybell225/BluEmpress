#!/usr/bin/env python3
"""Validate every JSON file in /data against its schema in /data/schema.

Also fails if a data file contains an email address, a long token-like string,
or a private URL. Read-only: this script never writes anything.
"""
import json, re, sys, pathlib
from jsonschema import Draft202012Validator

root = pathlib.Path(__file__).resolve().parent.parent / "data"
errors = []
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}")
SECRET = re.compile(r"(AIza[0-9A-Za-z_-]{20,}|sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|-----BEGIN [A-Z ]*PRIVATE KEY-----|[A-Za-z0-9+/_-]{40,})")

def load(path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(root.parent)}: invalid JSON ({exc})")

for schema_path in sorted((root / "schema").glob("*.schema.json")):
    schema = load(schema_path)
    if schema is None:
        continue
    name = schema_path.name.replace(".schema.json", "")
    data_path = root / f"{name}.json"
    if not data_path.exists():
        errors.append(f"missing data file for schema {schema_path.name}")
        continue
    data = load(data_path)
    if data is None:
        continue
    for err in Draft202012Validator(schema).iter_errors(data):
        where = "/".join(str(p) for p in err.absolute_path) or "(root)"
        errors.append(f"{data_path.name}: {where}: {err.message}")

for path in sorted(root.rglob("*.json")):
    if load(path) is None:
        continue
    text = path.read_text(encoding="utf-8")
    if EMAIL.search(text):
        errors.append(f"{path.name}: contains something that looks like an email address")
    # Public https links (like the signup form) may contain long ids, so ignore them.
    without_urls = re.sub(r"https://[^\s\"]+", "", text)
    if SECRET.search(without_urls):
        errors.append(f"{path.name}: contains a long token-like string")

if errors:
    print("JSON validation failed:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("All JSON data files are valid.")
