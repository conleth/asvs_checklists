🔴 **Level 3**

# ASVS 3 Checklist – general – frontend

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V10**

- [ ] **V10.2.3** – Verify that the OAuth client only requests the required scopes (or other authorization parameters) in requests to the authorization server.

- [ ] **V10.3.5** – Verify that the resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP).

- [ ] **V10.4.15** – Verify that, for a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it. For example, by requiring the usage of pushed authorization request (PAR) or JWT-secured Authorization Request (JAR).

- [ ] **V10.4.16** – Verify that the client is confidential and the authorization server requires the use of strong client authentication methods (based on public-key cryptography and resistant to replay attacks), such as mutual TLS ('tls_client_auth', 'self_signed_tls_client_auth') or private key JWT ('private_key_jwt').


🎯 **ASVS V11**

- [ ] **V11.2.4** – Verify that all cryptographic operations are constant-time, with no 'short-circuit' operations in comparisons, calculations, or returns, to avoid leaking information.

- [ ] **V11.5.2** – Verify that the random number generation mechanism in use is designed to work securely, even under heavy demand.


🎯 **ASVS V12**

- [ ] **V12.1.4** – Verify that proper certification revocation, such as Online Certificate Status Protocol (OCSP) Stapling, is enabled and configured.


🎯 **ASVS V13**

- [ ] **V13.1.4** – Verify that the application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and business requirements.


🎯 **ASVS V14**

- [ ] **V14.2.6** – Verify that the application only returns the minimum required sensitive data for the application's functionality. For example, only returning some of the digits of a credit card number and not the full number. If the complete data is required, it should be masked in the user interface unless the user specifically views it.

- [ ] **V14.2.7** – Verify that sensitive information is subject to data retention classification, ensuring that outdated or unnecessary data is deleted automatically, on a defined schedule, or as the situation requires.


🎯 **ASVS V2**

- [ ] **V2.3.5** – Verify that high-value business logic flows require multi-user approval to prevent unauthorized or accidental actions. This could include but is not limited to large monetary transfers, contract approvals, access to classified information, or safety overrides in manufacturing.

- [ ] **V2.4.2** – Verify that business logic flows require realistic human timing, preventing excessively rapid transaction submissions.


🎯 **ASVS V3**

- [ ] **V3.1.1** – Verify that application documentation states the expected security features that browsers using the application must support (such as HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), and other relevant HTTP security mechanisms). It must also define how the application must behave when some of these features are not available (such as warning the user or blocking access).

- [ ] **V3.3.5** – Verify that when the application writes a cookie, the cookie name and value length combined are not over 4096 bytes. Overly large cookies will not be stored by the browser and therefore not sent with requests, preventing the user from using application functionality which relies on that cookie.

- [ ] **V3.4.8** – Verify that all HTTP responses that initiate a document rendering (such as responses with Content-Type text/html), include the Cross‑Origin‑Opener‑Policy header field with the same-origin directive or the same-origin-allow-popups directive as required. This prevents attacks that abuse shared access to Window objects, such as tabnabbing and frame counting.

- [ ] **V3.5.6** – Verify that JSONP functionality is not enabled anywhere across the application to avoid Cross-Site Script Inclusion (XSSI) attacks.

- [ ] **V3.5.8** – Verify that authenticated resources (such as images, videos, scripts, and other documents) can be loaded or embedded on behalf of the user only when intended. This can be accomplished by strict validation of the Sec-Fetch-* HTTP request header fields to ensure that the request did not originate from an inappropriate cross-origin call, or by setting a restrictive Cross-Origin-Resource-Policy HTTP response header field to instruct the browser to block returned content.

- [ ] **V3.7.4** – Verify that the application's top-level domain (e.g., site.tld) is added to the public preload list for HTTP Strict Transport Security (HSTS). This ensures that the use of TLS for the application is built directly into the main browsers, rather than relying only on the Strict-Transport-Security response header field.

- [ ] **V3.7.5** – Verify that the application behaves as documented (such as warning the user or blocking access) if the browser used to access the application does not support the expected security features.


🎯 **ASVS V4**

- [ ] **V4.2.5** – Verify that, if the application (backend or frontend) builds and sends requests, it uses validation, sanitization, or other mechanisms to avoid creating URIs (such as for API calls) or HTTP request header fields (such as Authorization or Cookie), which are too long to be accepted by the receiving component. This could cause a denial of service, such as when sending an overly long request (e.g., a long cookie header field), which results in the server always responding with an error status.


🎯 **ASVS V5**

- [ ] **V5.2.5** – Verify that the application does not allow uploading compressed files containing symlinks unless this is specifically required (in which case it will be necessary to enforce an allowlist of the files that can be symlinked to).


🎯 **ASVS V7**

- [ ] **V7.5.3** – Verify that the application requires further authentication with at least one factor or secondary verification before performing highly sensitive transactions or operations.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
