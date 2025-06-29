# 🛡️ Context: AppSec Enablement at Scale — **Copilot Authoring Guide**

As the application security lead for a large enterprise (10,000+ developers), I am operationalizing **OWASP ASVS 5.0** across our engineering organisation. This file is injected into **every GitHub Copilot Chat prompt** in this repository—follow it faithfully so that the generated Python script and Markdown check‑lists remain consistent, predictable, and review‑ready.

---

## 0  Quick Mission Recap

* **Input**  ASVS 5.0 JSON (`OWASP_Application_Security_Verification_Standard_5.0.0_en.json`).
* **Output** A *complete* tree of Markdown check‑lists:

  ```
  ```

/checklists/{levelN}/{language}/{role}.md

````
Every possible **Level × Language × Role** file must exist, either with mapped controls or the fallback block (§ 6).
* **Why**  These files gate design reviews, pull‑requests, Security‑Champion workflows and CI quality checks.

---

## 1  🎯 Goal (unchanged)
Use the official JSON and generate the check‑lists exactly as shown. Each file must contain:
1. **Title** — `ASVS {LEVEL} Checklist – {LANGUAGE} – {ROLE}`
2. **Header** —
 > *Use during DESIGN and PRE‑MERGE review. This list is tailored to your stack and responsibility.*
3. **Body** — bullet list of mapped ASVS controls *or* the fallback (§ 6).

---

## 2  🗂️ JSON Anatomy (reminder)
Controls live at `.Items[].Items[].Items[]` and expose:
* `Shortcode` (e.g. `"V1.2.1"`)
* `Description` (full text)
* `L` – ASVS level (`"1"`, `"2"`, `"3"`)

---

## 3  🧠 Role Mapping — Keywords & Synonyms
| Role            | Primary Keywords | Extra Synonyms Copilot **should** detect |
|-----------------|------------------|------------------------------------------|
| `frontend`      | html, css, react, vue, dom, browser, xss, csp, ui, javascript | csp, service‑worker, web storage, localstorage |
| `backend`       | auth, authorization, sql, database, session, crypto, validation, orm | rdbms, jdbc, hibernate, entity, password hash |
| `api`           | rest, graphql, api, endpoint, json, rate limit, payload, websocket | openapi, grpc, webhook, idempotency, throttling |
| `integration`   | oauth, saml, openid, federation, identity, external, idp, sso | oidc, ws‑trust, sp‑initiated, id‑token |
| `mobile`        | android, ios, mobile, device, native | keystore, keychain, deeplink, apk, ipa |
| `platform`      | terraform, helm, deployment, cloud, kubernetes, docker, yaml, iac | helm‑chart, k8s‑manifest, cloud‑formation |
| `security`      | encryption, key management, hsm, secure store, jwt, hash, secrets, crypto, kms | key vault, vault, ssl, tls, certificate |
| `data`          | etl, data pipeline, bigquery, s3, data lake, csv, spark, pandas | parquet, warehouse, glue, airflow |
| `devsecops`     | pipeline, scan, sast, dast, dependency, artifact, veracode, semgrep, github actions | trivy, snyk, supply‑chain, sbom |
| `qa`            | unit test, fuzz, test coverage, selenium, mutation test, e2e | jest, junit, property‑based, fuzzing |
| `observability` | logging, trace, telemetry, monitor, alert, correlation, span | opentelemetry, promql, grafana, log injection |
| `devtools`      | sdk, cli, developer experience, internal tool, platform, documentation | api‑client, code‑gen, plugin |
| `mlops`         | model, ml, ai, training, serving, onnx, huggingface, model registry | feature‑store, prompt‑injection, data‑poisoning |
| `general`       | *(default if none above match)* | — |

> **Heuristic upgrade** – When a control **implicitly** targets a role (e.g., mentions *“browser cookie SameSite”* → `frontend`) but none of the keywords appear verbatim, Copilot should still assign it to the most obvious role.

---

## 4  💻 Language Mapping & Security Pitfalls
| Language     | Keywords                                 | Critical Pitfalls & Cues |
|--------------|------------------------------------------|--------------------------|
| `java`       | java, jvm, spring                        | Deserialization (Java serializable), XXE, SSRF with `URLConnection`, JNDI injection (Log4Shell), unchecked `ObjectInputStream`, weak crypto defaults |
| `csharp`     | c#, .net, asp.net                        | ViewState tampering, unsafe `BinaryFormatter`, insecure XML `DataContractSerializer`, cert‑validation bypass, CSRF without antiforgery token, insecure cookie flags |
| `python`     | python, flask, django                    | `pickle` / `yaml.load`, flask debug, `subprocess` injection, Django template injection, hard‑coded secrets, deserialization via `PyYAML` |
| `javascript` | javascript, node, typescript, react, vue | Prototype pollution, ReDoS, `eval`/`Function`, DOM‑XSS, insecure JWT libraries, `child_process.exec`, path traversal via `fs` |
| `general`    | *default if none above match*            | Universal issues: input validation, access control, logging, transport security |

**Language Inference Rule** — If a control’s description references any pitfall above, Copilot should tag that control with the corresponding language even if the explicit keyword is missing.

---

## 5  📊 Level → Folder Mapping
| Level | Folder   | Inheritance                        |
|-------|----------|------------------------------------|
| 1     | level1   | Appears in **1, 2, 3**             |
| 2     | level2   | Appears in **2, 3**                |
| 3     | level3   | Appears **only** in 3              |

---

## 6  🆕 Mandatory Handling of Empty Check‑lists
When **no controls match** a `{language}/{role}` slice **still create the file** and insert exactly:
```markdown
> ⚠️ **No ASVS items map to this language/role.**  
> Review the *General* checklist for Level {LEVEL} and your team’s secure‑coding guidelines.
````

*Never* omit a file or leave it blank.

---

## 7  🌐 ASVS Category → Role/Language Cheat‑Sheet

Copilot can use this table to infer mappings when keywords are sparse:

| ASVS Category (root V\*)     | Likely Roles                         | Likely Languages                         |
| ---------------------------- | ------------------------------------ | ---------------------------------------- |
| V1 Encoding & Injection      | `frontend`, `backend`, `api`         | all                                      |
| V2 Validation & Logic        | `backend`, `api`, `qa`               | all                                      |
| V3 Web Frontend              | `frontend`                           | `javascript`                             |
| V4 API & Web Service         | `api`, `integration`                 | `java`, `csharp`, `python`, `javascript` |
| V5 File Handling             | `backend`, `data`                    | all                                      |
| V6 Authentication            | `backend`, `security`, `integration` | all                                      |
| V7 Session Management        | `backend`, `security`, `frontend`    | all                                      |
| V8 Access Control            | `backend`, `security`                | all                                      |
| V9 Cryptography              | `security`, `backend`                | `java`, `csharp`, `python`               |
| V10 Error Handling & Logging | `backend`, `observability`           | all                                      |
| V11 Data Protection          | `security`, `data`, `mobile`         | all                                      |
| V12 Communications           | `platform`, `security`               | all                                      |
| V13 Malicious Code           | `devsecops`, `platform`              | all                                      |
| V14 Configuration            | `platform`, `devsecops`, `backend`   | all                                      |

*These alignments are non‑exclusive; Copilot should combine them with keyword and pitfall heuristics.*

---

## 8  🤖 Agent‑Mode Generation Flow (Copilot‑self‑check)

1. **Load JSON** (or path passed via `--json`).
2. **Iterate levels 1‑3**.
3. **For each level → each language → each role**:

   1. Collect matching controls (keyword + heuristic tables).
   2. Compose Markdown with title, header, emoji, and either list or fallback block.
   3. Save to the canonical path.
4. Ensure idempotency (clean old files before write or overwrite deterministically).
5. Emit a summary to STDOUT: counts per file, empty‑file count.

---

## 9  ✅ Output Hygiene

* UTF‑8, Unix newlines, trailing newline.
* Wrap lines ≤ 120 chars.
* No trailing whitespace.
* Prefer descriptive commit messages (`feat: generate ASVS check‑lists`).

---

## 🎁 Bonus (unchanged)

* `<details>` *Defense‑in‑Depth* section.
* Emoji indicators.
* Root‑level `README.md` linking to all check‑lists.

---

## 🧪 Final Task — Script Specs (reminder)

Write an **idempotent** Python 3.11+ script using only stdlib (`json`, `os`, `pathlib`, `collections`, `shutil`). Accept `--json` to override source path.

---

*End of Copilot Authoring Guide (v2 – smarter mapping).*

---

## 10  🎨 Visual Conventions (emojis)

* **Level badge** — At the very top of each checklist file, Copilot must include the level‑color badge:

  * 🟢 **Level 1**
  * 🟡 **Level 2**
  * 🔴 **Level 3**
* **Fallback note** — When a file has no mapped controls, the placeholder block MUST start with ⚠️ to draw attention:

  ```markdown
  > ⚠️ **No ASVS items match this language/role.**  
  > Review the General checklist for Level {LEVEL}.
  ```
* **Chapter separation** — Insert 🎯 before each ASVS chapter heading inside the file to make long lists more scannable.

These conventions are mandatory so reviewers can spot level, emptiness, and chapter boundaries at a glance.
