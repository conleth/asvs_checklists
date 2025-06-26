🔴 **Level 3**

# ASVS 3 Checklist – javascript – frontend

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V11**

- [ ] **V11.1.4** – Verify that a cryptographic inventory is maintained. This must include a documented plan that outlines the migration path to new cryptographic standards, such as post-quantum cryptography, in order to react to future threats.


🎯 **ASVS V3**

- [ ] **V3.2.3** – Verify that the application avoids DOM clobbering when using client-side JavaScript by employing explicit variable declarations, performing strict type checking, avoiding storing global variables on the document object, and implementing namespace isolation.

- [ ] **V3.5.7** – Verify that data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks.

- [ ] **V3.6.1** – Verify that client-side assets, such as JavaScript libraries, CSS, or web fonts, are only hosted externally (e.g., on a Content Delivery Network) if the resource is static and versioned and Subresource Integrity (SRI) is used to validate the integrity of the asset. If this is not possible, there should be a documented security decision to justify this for each resource.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
