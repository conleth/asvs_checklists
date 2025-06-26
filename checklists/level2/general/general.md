🟡 **Level 2**

# ASVS 2 Checklist – general – general

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V1**

- [ ] **V1.2.9** – Verify that the application escapes special characters in regular expressions (typically using a backslash) to prevent them from being misinterpreted as metacharacters.

- [ ] **V1.3.3** – Verify that data being passed to a potentially dangerous context is sanitized beforehand to enforce safety measures, such as only allowing characters which are safe for this context and trimming input which is too long.

- [ ] **V1.3.9** – Verify that the application sanitizes content before it is sent to memcache to prevent injection attacks.

- [ ] **V1.4.1** – Verify that the application uses memory-safe string, safer memory copy and pointer arithmetic to detect or prevent stack, buffer, or heap overflows.

- [ ] **V1.4.3** – Verify that dynamically allocated memory and resources are released, and that references or pointers to freed memory are removed or set to null to prevent dangling pointers and use-after-free vulnerabilities.


🎯 **ASVS V10**

- [ ] **V10.4.8** – Verify that refresh tokens have an absolute expiration, including if sliding refresh token expiration is applied.


🎯 **ASVS V12**

- [ ] **V12.3.4** – Verify that TLS connections between internal services use trusted certificates. Where internally generated or self-signed certificates are used, the consuming service must be configured to only trust specific internal CAs and specific self-signed certificates.


🎯 **ASVS V13**

- [ ] **V13.2.5** – Verify that the web or application server is configured with an allowlist of resources or systems to which the server can send requests or load data or files from.

- [ ] **V13.3.2** – Verify that access to secret assets adheres to the principle of least privilege.


🎯 **ASVS V14**

- [ ] **V14.2.2** – Verify that the application prevents sensitive data from being cached in server components, such as load balancers and application caches, or ensures that the data is securely purged after use.

- [ ] **V14.2.3** – Verify that defined sensitive data is not sent to untrusted parties (e.g., user trackers) to prevent unwanted collection of data outside of the application's control.


🎯 **ASVS V16**

- [ ] **V16.2.3** – Verify that the application only stores or broadcasts logs to the files and services that are documented in the log inventory.


🎯 **ASVS V17**

- [ ] **V17.1.1** – Verify that the Traversal Using Relays around NAT (TURN) service only allows access to IP addresses that are not reserved for special purposes (e.g., internal networks, broadcast, loopback). Note that this applies to both IPv4 and IPv6 addresses.


🎯 **ASVS V2**

- [ ] **V2.2.3** – Verify that the application ensures that combinations of related data items are reasonable according to the pre-defined rules.

- [ ] **V2.3.3** – Verify that transactions are being used at the business logic level such that either a business logic operation succeeds in its entirety or it is rolled back to the previous correct state.

- [ ] **V2.3.4** – Verify that business logic level locking mechanisms are used to ensure that limited quantity resources (such as theater seats or delivery slots) cannot be double-booked by manipulating the application's logic.


🎯 **ASVS V3**

- [ ] **V3.3.3** – Verify that cookies have the '__Host-' prefix for the cookie name unless they are explicitly designed to be shared with other hosts.

- [ ] **V3.5.5** – Verify that messages received by the postMessage interface are discarded if the origin of the message is not trusted, or if the syntax of the message is invalid.


🎯 **ASVS V4**

- [ ] **V4.1.3** – Verify that any HTTP header field used by the application and set by an intermediary layer, such as a load balancer, a web proxy, or a backend-for-frontend service, cannot be overridden by the end-user. Example headers might include X-Real-IP, X-Forwarded-*, or X-User-ID.

- [ ] **V4.2.1** – Verify that all application components (including load balancers, firewalls, and application servers) determine boundaries of incoming HTTP messages using the appropriate mechanism for the HTTP version to prevent HTTP request smuggling. In HTTP/1.x, if a Transfer-Encoding header field is present, the Content-Length header must be ignored per RFC 2616. When using HTTP/2 or HTTP/3, if a Content-Length header field is present, the receiver must ensure that it is consistent with the length of the DATA frames.


🎯 **ASVS V6**

- [ ] **V6.1.2** – Verify that a list of context-specific words is documented in order to prevent their use in passwords. The list could include permutations of organization names, product names, system identifiers, project codenames, department or role names, and similar.

- [ ] **V6.2.11** – Verify that the documented list of context specific words is used to prevent easy to guess passwords being created.

- [ ] **V6.2.9** – Verify that passwords of at least 64 characters are permitted.


🎯 **ASVS V8**

- [ ] **V8.4.1** – Verify that multi-tenant applications use cross-tenant controls to ensure consumer operations will never affect tenants with which they do not have permissions to interact.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
