🔴 **Level 3**

# ASVS 3 Checklist – general – security

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V10**

- [ ] **V10.4.12** – Verify that for a given client, the authorization server only allows the 'response_mode' value that this client needs to use. For example, by having the authorization server validate this value against the expected values or by using pushed authorization request (PAR) or JWT-secured Authorization Request (JAR).

- [ ] **V10.4.15** – Verify that, for a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it. For example, by requiring the usage of pushed authorization request (PAR) or JWT-secured Authorization Request (JAR).

- [ ] **V10.4.16** – Verify that the client is confidential and the authorization server requires the use of strong client authentication methods (based on public-key cryptography and resistant to replay attacks), such as mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') or private key JWT ('private_key_jwt').


🎯 **ASVS V11**

- [ ] **V11.1.3** – Verify that cryptographic discovery mechanisms are employed to identify all instances of cryptography in the system, including encryption, hashing, and signing operations.

- [ ] **V11.2.4** – Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information.

- [ ] **V11.2.5** – Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities, such as Padding Oracle attacks.

- [ ] **V11.3.4** – Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair. The method of generation must be appropriate for the algorithm being used.

- [ ] **V11.3.5** – Verify that any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode.

- [ ] **V11.6.2** – Verify that approved cryptographic algorithms are used for key exchange (such as Diffie-Hellman) with a focus on ensuring that key exchange mechanisms use secure parameters. This will prevent attacks on the key establishment process which could lead to adversary-in-the-middle attacks or cryptographic breaks.

- [ ] **V11.7.1** – Verify that full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes.


🎯 **ASVS V13**

- [ ] **V13.1.4** – Verify that the application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and business requirements.

- [ ] **V13.3.3** – Verify that all cryptographic operations are performed using an isolated security module (such as a vault or hardware security module) to securely manage and protect key material from exposure outside of the security module.

- [ ] **V13.3.4** – Verify that secrets are configured to expire and be rotated based on the application's documentation.


🎯 **ASVS V6**

- [ ] **V6.7.1** – Verify that the certificates used to verify cryptographic authentication assertions are stored in a way protects them from modification.

- [ ] **V6.7.2** – Verify that the challenge nonce is at least 64 bits in length, and statistically unique or unique over the lifetime of the cryptographic device.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
