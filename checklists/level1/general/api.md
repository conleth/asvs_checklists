🟢 **Level 1**

# ASVS 1 Checklist – general – api

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V1**

- [ ] **V1.5.1** – Verify that the application configures XML parsers to use a restrictive configuration and that unsafe features such as resolving external entities are disabled to prevent XML eXternal Entity (XXE) attacks.


🎯 **ASVS V14**

- [ ] **V14.2.1** – Verify that sensitive data is only sent to the server in the HTTP message body or header fields, and that the URL and query string do not contain sensitive information, such as an API key or session token.


🎯 **ASVS V3**

- [ ] **V3.2.1** – Verify that security controls are in place to prevent browsers from rendering content or functionality in HTTP responses in an incorrect context (e.g., when an API, a user-uploaded file or other resource is requested directly). Possible controls could include: not serving the content unless HTTP request header fields (such as Sec-Fetch-\*) indicate it is the correct context, using the sandbox directive of the Content-Security-Policy header field or using the attachment disposition type in the Content-Disposition header field.


🎯 **ASVS V4**

- [ ] **V4.4.1** – Verify that WebSocket over TLS (WSS) is used for all WebSocket connections.


🎯 **ASVS V6**

- [ ] **V6.1.1** – Verify that application documentation defines how controls such as rate limiting, anti-automation, and adaptive response, are used to defend against attacks such as credential stuffing and password brute force. The documentation must make clear how these controls are configured and prevent malicious account lockout.


🎯 **ASVS V7**

- [ ] **V7.2.2** – Verify that the application uses either self-contained or reference tokens that are dynamically generated for session management, i.e. not using static API secrets and keys.


🎯 **ASVS V8**

- [ ] **V8.1.1** – Verify that authorization documentation defines rules for restricting function-level and data-specific access based on consumer permissions and resource attributes.

- [ ] **V8.2.1** – Verify that the application ensures that function-level access is restricted to consumers with explicit permissions.

- [ ] **V8.2.2** – Verify that the application ensures that data-specific access is restricted to consumers with explicit permissions to specific data items to mitigate insecure direct object reference (IDOR) and broken object level authorization (BOLA).

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
