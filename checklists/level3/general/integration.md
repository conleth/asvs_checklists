🔴 **Level 3**

# ASVS 3 Checklist – general – integration

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V10**

- [ ] **V10.2.3** – Verify that the OAuth client only requests the required scopes (or other authorization parameters) in requests to the authorization server.

- [ ] **V10.3.5** – Verify that the resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP).


🎯 **ASVS V12**

- [ ] **V12.3.5** – Verify that services communicating internally within a system (intra-service communications) use strong authentication to ensure that each endpoint is verified. Strong authentication methods, such as TLS client authentication, must be employed to ensure identity, using public-key infrastructure and mechanisms that are resistant to replay attacks. For microservice architectures, consider using a service mesh to simplify certificate management and enhance security.


🎯 **ASVS V13**

- [ ] **V13.1.3** – Verify that the application documentation defines resource‑management strategies for every external system or service it uses (e.g., databases, file handles, threads, HTTP connections). This should include resource‑release procedures, timeout settings, failure handling, and where retry logic is implemented, specifying retry limits, delays, and back‑off algorithms. For synchronous HTTP request–response operations it should mandate short timeouts and either disable retries or strictly limit retries to prevent cascading delays and resource exhaustion.


🎯 **ASVS V15**

- [ ] **V15.2.4** – Verify that third-party components and all of their transitive dependencies are included from the expected repository, whether internally owned or an external source, and that there is no risk of a dependency confusion attack.

- [ ] **V15.4.3** – Verify that locks are used consistently to avoid threads getting stuck, whether by waiting on each other or retrying endlessly, and that locking logic stays within the code responsible for managing the resource to ensure locks cannot be inadvertently or maliciously modified by external classes or code.


🎯 **ASVS V17**

- [ ] **V17.2.7** – Verify that any audio or video recording mechanisms associated with the media server are able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users.


🎯 **ASVS V8**

- [ ] **V8.4.2** – Verify that access to administrative interfaces incorporates multiple layers of security, including continuous consumer identity verification, device security posture assessment, and contextual risk analysis, ensuring that network location or trusted endpoints are not the sole factors for authorization even though they may reduce the likelihood of unauthorized access.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
