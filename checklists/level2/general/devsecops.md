# 🟡 ASVS 2 Checklist – general – devsecops

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*


- [ ] **V13.3.1** – Verify that a secrets management solution, such as a key vault, is used to securely create, store, control access to, and destroy backend secrets. These could include passwords, key material, integrations with databases and third-party systems, keys and seeds for time-based tokens, other internal secrets, and API keys. Secrets must not be included in application source code or included in build artifacts. For an L3 application, this must involve a hardware-backed solution such as an HSM.

- [ ] **V5.4.3** – Verify that files obtained from untrusted sources are scanned by antivirus scanners to prevent serving of known malicious content.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
