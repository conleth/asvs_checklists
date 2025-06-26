# 🟢 ASVS 1 Checklist – general – integration

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*


- [ ] **V1.5.1** – Verify that the application configures XML parsers to use a restrictive configuration and that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks.

- [ ] **V12.2.1** – Verify that TLS is used for all connectivity between a client and external facing, HTTP-based services, and does not fall back to insecure or unencrypted communications.

- [ ] **V12.2.2** – Verify that external facing services use publicly trusted TLS certificates.

- [ ] **V13.4.1** – Verify that the application is deployed either without any source control metadata, including the .git or .svn folders, or in a way that these folders are inaccessible both externally and to the application itself.

- [ ] **V6.2.7** – Verify that "paste" functionality, browser password helpers, and external password managers are permitted.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
