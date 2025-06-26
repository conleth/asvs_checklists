# OWASP ASVS Check‑lists – Usage Guide

**Version:** 5.0.0  |  **Aligned standard:** [OWASP Application Security Verification Standard v5.0.0](https://owasp.org/www-project-application-security-verification-standard/)  |  **Last updated:** 26 June 2025

---

## 1  Why these check‑lists exist

These Markdown files distil the complete set of 345 normative OWASP ASVS controls into actionable, role‑friendly check‑lists that teams can embed directly into their day‑to‑day workflow (pull‑request templates, Confluence pages, sprint DoDs, etc.).  They provide **full coverage** of ASVS while minimising duplication and language noise.

*Use them to verify that every new or changed feature meets the agreed assurance level before it is merged, released, or put into production.*

---

## 2  Folder & file structure

```text
checklists/
├── level1/          # ASVS Level 1 – basic security hygiene
│   ├── general/     # Language‑agnostic controls (70 items)
│   ├── java/        # Java/JVM‑specific add‑ons (≤ 15 items)
│   └── javascript/  # JavaScript/Node/TS add‑ons  (≤ 15 items)
├── level2/          # ASVS Level 2 – internet‑facing business apps
│   └── …            # Same sub‑structure
└── level3/          # ASVS Level 3 – critical / high‑value apps
    └── …
```

* **`general/`** contains \~95 % of the requirements for the level.
* Language folders add only the few stack‑specific controls.

> **Rule of thumb:** **General + your stack folder = 100 % of what you must verify.**

---

## 3  How to select the right checklist(s)

| If you are…                                                                      | Then open…                                                                        | Example                                     |
| -------------------------------------------------------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------- |
| **Backend engineer** working on a Java micro‑service that must meet Level 2      | `level2/general/backend.md` **plus** `level2/java/backend.md`                     | `- [ ] V5.1.2  Use parameterised queries …` |
| **Frontend engineer** writing React for a public portal (Level 1)                | `level1/general/frontend.md` + `level1/javascript/frontend.md`                    |                                             |
| **Security reviewer** performing a design review for a critical system (Level 3) | Every file under `level3/general/` (backend, frontend, API, infrastructure, etc.) |                                             |

> 🛈 **Tip**: Pin the two files to your IDE or merge‑request template so you never forget a control.

---

## 4  When to apply the checks

| SDLC phase                         | Minimal recommended action                                                                                  |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| **Requirements**                   | Check only the *architecture* & *deployment* files to ensure planned features do not violate core controls. |
| **Design**                         | Walk through all relevant files; flag controls that need explicit design artefacts (e.g.                    | threat‑model diagrams). |
| **Code review / Merge request**    | Reviewer verifies every box is ticked and evidence (test, scan report, commit link) is recorded.            |
| **Pre‑release / Security testing** | Confirm nothing is left unchecked; attach penetration‑test findings to the same list.                       |
| **Operations & maintenance**       | Re‑run the list after major infra changes or annually, whichever comes first.                               |

> **Zero‑defect policy:** No release goes live with an unchecked ❑ or a ✗ in any mandatory (🟥) item.

---

## 5  Reading the items

Each line follows the pattern

```markdown
- [ ] V11.4.2 | 🟥 MUST | *Passwords are stored using an approved, computationally intensive key derivation function (e.g., Argon2id) with parameters set per current guidance.*
      ^checkbox   ^priority ^requirement text (verbatim from ASVS)
```

* **Checkbox** – tick once the control is demonstrably satisfied **for this change**.
* **Code (e.g. `V2.1.3`)** – stable identifier; links back to the ASVS PDF/HTML.
* **Priority badge (optional)** – 🟥 MUST, 🟧 SHOULD, 🟩 MAY.  Default is **MUST** if no badge present.  Tune these to your risk appetite.
* **Text** – exact wording from ASVS v5.0.0, ensuring no interpretation drift.

### Linking back to the standard

Add an inline link if you need deeper context, e.g.

```markdown
- [ ] V4.3.1 | 🟥 MUST | *All credentials are stored “hashed + salted” ([ASVS V4.3.1](https://owasp.org/…/v4.3.1))*
```

---

## 6  Practical integration examples

### 6.1  GitHub pull‑request template

```yaml
# .github/PULL_REQUEST_TEMPLATE/security-checklist.md
name: "Security checklist (ASVS L2 – Java)"
body:
  - type: markdown
    attributes:
      value: |
        Copy the two files below and tick everything before requesting review.
  - type: checkboxes
    attributes:
      label: "General backend security (L2)"
      options:
        - label: "Paste content of level2/general/backend.md here"
  - type: checkboxes
    attributes:
      label: "Java specific controls (L2)"
      options:
        - label: "Paste content of level2/java/backend.md here"
```

### 6.2  Confluence / SharePoint page

1. Create a new page per checklist.
2. Enable *Tasklist* or *Checkboxes* macro.
3. Paste the Markdown – Confluence auto‑converts to rich text.
4. Require developers to attach evidence links next to each item.

### 6.3  CI gate (optional)

Export your check‑lists to JSON and fail the pipeline if mandatory items are unchecked.  Minimal example:

```bash
python tools/extract_unchecked.py level2 > unchecked.txt
if grep -q "| 🟥" unchecked.txt; then
  echo "Blocking build: mandatory controls missing" && exit 1
fi
if grep -q "| 🟧" unchecked.txt; then
  echo "⚠︎ Recommended controls (🟧) remain unchecked — please review before merge."
fi
```

---

## 7  Versioning & update policy

| Event                           | Action                                                               |
| ------------------------------- | -------------------------------------------------------------------- |
| OWASP releases new ASVS version | Track diff, update affected lines **ideally within 30 days**; raise an exception ticket if the diff affects more than 50 lines or requires code changes. |
| New language/stack is adopted   | Add a folder (e.g. `python/`) and include only stack‑specific items. |
| Internal risk/guidelines change | Adjust priority badges; never change ASVS wording itself.            |

All changes must be reviewed by AppSec and version‑tagged (e.g. `v5.0.1-ourorg`).

---

## 8  Contributing

1. **Fork + branch → PR** – same as code.
2. Describe *why* (new stack, bug, missing link, etc.).
3. One approval from AppSec + one from an engineer of that stack required.

---

## 9  License

These check‑lists are derived from OWASP ASVS, which is licensed under the [Creative Commons Attribution‑ShareAlike 4.0 International](https://creativecommons.org/licenses/by-sa/4.0/) (CC BY‑SA 4.0).  Your organisation’s additions are licensed under the same terms unless explicitly stated otherwise.

---

## 10  References & further reading

* `OWASP_Application_Security_Verification_Standard_5.0.0_en.json` – machine‑readable source for tooling
* [OWASP ASVS Project](https://owasp.org/www-project-application-security-verification-standard/)
* [Cheat Sheet Series](https://cheatsheetseries.owasp.org/) – implementation guidance for many controls
* [OWASP SAMM](https://owasp.org/www-project-samm/) – security‑practice maturity model (macro‑level)
* *Secure Coding in C & C++* (Seacord) – background reading for stack‑independent best practices

---

**Happy secure coding!**
