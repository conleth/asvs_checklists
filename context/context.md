# 🛡️ Context: AppSec Enablement at Scale

As the application security lead for a large enterprise (10,000+ developers), I am operationalizing OWASP ASVS 5.0 across our engineering org. I need to break down ASVS controls into actionable Markdown checklists that are customized per:

* Developer role
* Programming language/tech stack
* Security tier (mapped to ASVS Level 1–3)

These checklists will be embedded into design reviews, PR templates, security champion tooling, and CI quality gates.

---

# 🎯 Goal

Use the official `OWASP_Application_Security_Verification_Standard_5.0.0_en.json` file and:

✅ Generate Markdown checklist files like this:

```
/checklists/{asvs_level}/{language}/{role}.md
```

Each checklist should include:

* A title: `ASVS {LEVEL} Checklist – {LANGUAGE} – {ROLE}`
* A header:

  > "*Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility.*"
* A bullet list like:

  ```
  - [ ] V1.2.1 – Verify that user input is properly validated and encoded …
  ```

---

# 🧱 JSON Input Structure

* Top-level key: `Requirements`
* Controls are nested inside `.Items[].Items[].Items[]`
* Each control has:

  * "Shortcode" (e.g., "V1.2.1")
  * "Description" (the text of the requirement)
  * "L" (ASVS level: "1", "2", or "3")

---

# 🧠 Role Mapping (Expanded for Enterprise Teams)

Determine roles using keyword matching from the control’s `Description`. Each control may belong to multiple roles:

| Role            | Keywords                                                                            |
| --------------- | ----------------------------------------------------------------------------------- |
| `frontend`      | html, css, react, vue, dom, browser, xss, csp, ui, javascript                       |
| `backend`       | auth, authorization, sql, database, session, crypto, validation, orm                |
| `api`           | rest, graphql, api, endpoint, json, rate limit, payload, websocket                  |
| `integration`   | oauth, saml, openid, federation, identity, external, idp, sso                       |
| `mobile`        | android, ios, mobile, device, native                                                |
| `platform`      | terraform, helm, deployment, cloud, kubernetes, docker, yaml, iac                   |
| `security`      | encryption, key management, hsm, secure store, jwt, hash, secrets, crypto, kms      |
| `data`          | etl, data pipeline, bigquery, s3, data lake, csv, spark, pandas                     |
| `devsecops`     | pipeline, scan, sast, dast, dependency, artifact, veracode, semgrep, github actions |
| `qa`            | unit test, fuzz, test coverage, selenium, mutation test, e2e, integration test      |
| `observability` | logging, trace, telemetry, monitor, alert, correlation, span, observability         |
| `devtools`      | sdk, cli, developer experience, internal tool, platform, documentation              |
| `mlops`         | model, ml, ai, training, serving, onnx, huggingface, model registry                 |
| `general`       | default if no match above                                                           |

---

# 💻 Language Mapping

| Language     | Keywords                                 |
| ------------ | ---------------------------------------- |
| `java`       | java, jvm, spring                        |
| `csharp`     | c#, .net, asp.net                        |
| `python`     | python, flask, django                    |
| `javascript` | javascript, node, typescript, react, vue |
| `general`    | default if no match                      |

---

# 📊 ASVS Level Mapping

| Level | Output Folder                              |
| ----- | ------------------------------------------ |
| `1`   | `level1` (must be included in 1, 2, and 3) |
| `2`   | `level2` (included in 2 and 3)             |
| `3`   | `level3` (only in 3)                       |

Higher tiers inherit lower-tier rules.

---

# ✅ Output Requirements

* Clean folder structure under `/`
* Each Markdown file is valid GitHub-flavored Markdown
* (Optional): Create a `README.md` at the root that links to each checklist

---

# 📎 Example Output Structure

```
/checklists/
├── level1/
│   ├── python/
│   │   ├── backend.md
│   │   └── devsecops.md
│   └── javascript/
│       └── frontend.md
├── level2/
├── level3/
```

---

# 🎁 Bonus (optional)

<!-- - Generate a CSV with: `Shortcode`, `Description`, `Level`, `Roles`, `Languages`, `Checklist Files` -->

* Include a `<details>` section in Markdown files for advanced defense-in-depth guidance
* Add GitHub emoji indicators: 🟢 Level 1, 🟡 Level 2, 🔴 Level 3

---

# 🧪 Final Task

Write the Python script that does all of the above and saves the checklist outputs to disk. You can use `json`, `os`, `pathlib`, `collections`, and `shutil`. Let me know if you'd like test data or assistance with the folder structure.
