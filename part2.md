\#!/usr/bin/env python3
"""
update\_checklists.py — Generate OWASP ASVS 5.0.0 Markdown check‑lists
----------------------------------------------------------------------

This script converts the official JSON file (downloaded as
`OWASP_Application_Security_Verification_Standard_5.0.0_en.json`) into a set
of GitHub‑flavoured Markdown check‑lists arranged by
• ASVS level (1‒3)              →  /checklists/level{n}/
• Language / tech‑stack folder  →  /{language}/
• Role‐specific file            →  {role}.md

**NEW in v2 (2025‑06‑26)**
• Always generate every language/role combination for every level, even when
no controls match → empty checklist contains a placeholder notice.
• Idempotent: It rewrites files only when content changed.
• Emoji indicator of the level in the title (🟢 L1, 🟡 L2, 🔴 L3).

Run:
python update\_checklists.py \[path/to/ASVS.json]  # default in cwd

Dependencies: Only std‑lib (`json`, `pathlib`, `re`, `textwrap`, `argparse`).
"""
from **future** import annotations

import argparse
import json
import re
import textwrap
from collections import defaultdict
from pathlib import Path
from typing import Dict, List, Tuple

# ---------------------------------------------------------------------------

# CONFIGURATION (keep in sync with .github/copilot‑instructions.md)

# ---------------------------------------------------------------------------

ASVS\_VERSION = "5.0.0"
ASVS\_URL = "[https://owasp.org/www-project-application-security-verification-standard/](https://owasp.org/www-project-application-security-verification-standard/)"

LANGUAGE\_KEYWORDS: Dict\[str, List\[str]] = {
"java": \["java", "jvm", "spring"],
"csharp": \["c#", ".net", "asp.net"],
"python": \["python", "flask", "django"],
"javascript": \["javascript", "node", "typescript", "react", "vue"],
"general": \[],  # default bucket – always generated
}

ROLE\_KEYWORDS: Dict\[str, List\[str]] = {
"frontend": \["html", "css", "react", "vue", "dom", "browser", "xss", "csp", "ui", "javascript"],
"backend": \["auth", "authorization", "sql", "database", "session", "crypto", "validation", "orm"],
"api": \["rest", "graphql", "api", "endpoint", "json", "rate limit", "payload", "websocket"],
"integration": \["oauth", "saml", "openid", "federation", "identity", "external", "idp", "sso"],
"mobile": \["android", "ios", "mobile", "device", "native"],
"platform": \[
"terraform", "helm", "deployment", "cloud", "kubernetes", "docker", "yaml", "iac",
],
"security": \["encryption", "key management", "hsm", "secure store", "jwt", "hash", "secrets", "crypto", "kms"],
"data": \["etl", "data pipeline", "bigquery", "s3", "data lake", "csv", "spark", "pandas"],
"devsecops": \[
"pipeline", "scan", "sast", "dast", "dependency", "artifact", "veracode", "semgrep", "github actions",
],
"qa": \[
"unit test", "fuzz", "test coverage", "selenium", "mutation test", "e2e", "integration test",
],
"observability": \[
"logging", "trace", "telemetry", "monitor", "alert", "correlation", "span", "observability",
],
"devtools": \["sdk", "cli", "developer experience", "internal tool", "platform", "documentation"],
"mlops": \[
"model", "ml", "ai", "training", "serving", "onnx", "huggingface", "model registry",
],
"general": \[],  # default bucket
}

LEVEL\_EMOJI = {"1": "🟢", "2": "🟡", "3": "🔴"}

OUTPUT\_ROOT = Path("checklists")

HEADER\_TEXT = (
"*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*"
)
PLACEHOLDER\_TEXT = (
"> **No ASVS controls map to this language/role combination at the moment.**\n\n"
"> *This file is still generated for completeness so teams have a predictable folder structure.\n"
"> As the ASVS or mapping rules evolve, controls may appear here automatically.*"
)

# ---------------------------------------------------------------------------

# Utility helpers

# ---------------------------------------------------------------------------

def slugify(text: str) -> str:
return re.sub(r"\[^a-z0-9\_-]+", "-", text.lower()).strip("-")

def load\_asvs(json\_path: Path) -> List\[Dict]:
data = json.loads(json\_path.read\_text(encoding="utf-8"))
reqs = \[]

```
def walk(items):
    for item in items:
        if "Items" in item and item["Items"]:
            walk(item["Items"])
        else:
            reqs.append(item)

walk(data["Requirements"]["Items"])
return reqs
```

# ---------------------------------------------------------------------------

# Mapping logic

# ---------------------------------------------------------------------------

def match\_bucket(description: str, mapping: Dict\[str, List\[str]]) -> List\[str]:
desc\_lower = description.lower()
matches = \[bucket for bucket, keys in mapping.items() if any(k in desc\_lower for k in keys)]
return matches or \["general"]

def classify\_controls(controls: List\[Dict]) -> Dict\[Tuple\[str, str, str], List\[Dict]]:
"""Return dict keyed by (level, language, role) → list\[control]"""
buckets: Dict\[Tuple\[str, str, str], List\[Dict]] = defaultdict(list)

```
for ctrl in controls:
    level = str(ctrl["L"])
    shortcode = ctrl["Shortcode"]
    desc = ctrl["Description"].strip()

    languages = match_bucket(desc, LANGUAGE_KEYWORDS)
    roles = match_bucket(desc, ROLE_KEYWORDS)

    for lang in languages:
        for role in roles:
            buckets[(level, lang, role)].append({"code": shortcode, "desc": desc})
return buckets
```

# ---------------------------------------------------------------------------

# Markdown rendering helpers

# ---------------------------------------------------------------------------

def render\_markdown(level: str, language: str, role: str, controls: List\[Dict]) -> str:
emoji = LEVEL\_EMOJI\[level]
lines: List\[str] = \[]
lines.append(f"# {emoji} ASVS {level} Checklist – {language} – {role}\n")
lines.append(HEADER\_TEXT + "\n\n")

```
if controls:
    for ctrl in sorted(controls, key=lambda c: c["code"]):
        code = ctrl["code"]
        desc = ctrl["desc"].rstrip(".")
        lines.append(f"- [ ] **{code}** – {desc}.\n")
else:
    lines.append(PLACEHOLDER_TEXT + "\n")

# Advanced guidance section (collapsed details) – optional placeholder
lines.append("<details><summary>Advanced defense‑in‑depth guidance</summary>\n\n")
lines.append("_Add organisation‑specific recommendations, links to tooling, threat models, etc._\n")
lines.append("</details>\n\n")

lines.append("---\n")
lines.append(
    f"Generated from [OWASP ASVS {ASVS_VERSION}]({ASVS_URL}) on {Path(__file__).stat().st_mtime_ns}. "
    "Do not edit manually; run `update_checklists.py` instead."\n"
)
return "\n".join(lines)
```

# ---------------------------------------------------------------------------

# Main generation

# ---------------------------------------------------------------------------

def ensure\_all\_combinations() -> List\[Tuple\[str, str, str]]:
levels = \["1", "2", "3"]
all\_langs = list(LANGUAGE\_KEYWORDS.keys())
all\_roles = list(ROLE\_KEYWORDS.keys())
combos = \[(lvl, lang, role) for lvl in levels for lang in all\_langs for role in all\_roles]
return combos

def generate\_checklists(json\_path: Path):
controls = load\_asvs(json\_path)
bucketed = classify\_controls(controls)

```
for level, language, role in ensure_all_combinations():
    controls_here = bucketed.get((level, language, role), [])
    folder = OUTPUT_ROOT / f"level{level}" / language
    folder.mkdir(parents=True, exist_ok=True)
    file_path = folder / f"{role}.md"
    new_content = render_markdown(level, language, role, controls_here)

    if file_path.exists() and file_path.read_text(encoding="utf-8") == new_content:
        continue  # up‑to‑date
    file_path.write_text(new_content, encoding="utf-8")
    print("Updated", file_path)

# Optional: generate README linking to all checklists
readme_path = OUTPUT_ROOT / "README.md"
if not readme_path.exists():
    umbrella = [
        "# 🗂️ OWASP ASVS Check‑lists", "", "Autogenerated set of check‑lists organised by level, language and role.",
        "", "Run `python update_checklists.py` after updating the JSON or mapping tables.",
    ]
    readme_path.write_text("\n".join(umbrella), encoding="utf-8")
```

# ---------------------------------------------------------------------------

# CLI

# ---------------------------------------------------------------------------

def main():
parser = argparse.ArgumentParser(description="Generate OWASP ASVS Markdown check‑lists.")
parser.add\_argument(
"json", nargs="?", default="OWASP\_Application\_Security\_Verification\_Standard\_5.0.0\_en.json", help="Path to ASVS JSON file",
)
args = parser.parse\_args()

```
json_path = Path(args.json)
if not json_path.is_file():
    raise SystemExit(f"ASVS JSON file not found: {json_path}")

generate_checklists(json_path)
print("All check‑lists are up‑to‑date.")
```

if **name** == "**main**":
main()
