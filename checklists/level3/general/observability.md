🔴 **Level 3**

# ASVS 3 Checklist – general – observability

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V8**

- [ ] **V8.3.2** – Verify that changes to values on which authorization decisions are made are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in self-contained tokens), there must be mitigating controls to alert when a consumer performs an action when they are no longer authorized to do so and revert the change. Note that this alternative would not mitigate information leakage.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
