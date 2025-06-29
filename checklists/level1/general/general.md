🟢 **Level 1**

# ASVS 1 Checklist – general – general

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V11**

- [ ] **V11.3.1** – Verify that insecure block modes (e.g., ECB) and weak padding schemes (e.g., PKCS#1 v1.5) are not used.

- [ ] **V11.3.2** – Verify that only approved ciphers and modes such as AES with GCM are used.


🎯 **ASVS V12**

- [ ] **V12.1.1** – Verify that only the latest recommended versions of the TLS protocol are enabled, such as TLS 1.2 and TLS 1.3. The latest version of the TLS protocol must be the preferred option.


🎯 **ASVS V2**

- [ ] **V2.3.1** – Verify that the application will only process business logic flows for the same user in the expected sequential step order and without skipping steps.


🎯 **ASVS V3**

- [ ] **V3.3.1** – Verify that cookies have the 'Secure' attribute set, and if the '\__Host-' prefix is not used for the cookie name, the '__Secure-' prefix must be used for the cookie name.


🎯 **ASVS V5**

- [ ] **V5.3.1** – Verify that files uploaded or generated by untrusted input and stored in a public folder, are not executed as server-side program code when accessed directly with an HTTP request.


🎯 **ASVS V6**

- [ ] **V6.2.1** – Verify that user set passwords are at least 8 characters in length although a minimum of 15 characters is strongly recommended.

- [ ] **V6.2.2** – Verify that users can change their password.

- [ ] **V6.2.6** – Verify that password input fields use type=password to mask the entry. Applications may allow the user to temporarily view the entire masked password, or the last typed character of the password.

- [ ] **V6.3.2** – Verify that default user accounts (e.g., "root", "admin", or "sa") are not present in the application or are disabled.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
