🔴 **Level 3**

# ASVS 3 Checklist – general – mlops

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V1**

- [ ] **V1.2.10** – Verify that the application is protected against CSV and Formula Injection. The application must follow the escaping rules defined in RFC 4180 sections 2.6 and 2.7 when exporting CSV content. Additionally, when exporting to CSV or other spreadsheet formats (such as XLS, XLSX, or ODF), special characters (including '=', '+', '-', '@', '\t' (tab), and '\0' (null character)) must be escaped with a single quote if they appear as the first character in a field value.

- [ ] **V1.5.3** – Verify that different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks.


🎯 **ASVS V10**

- [ ] **V10.3.5** – Verify that the resource server prevents the use of stolen access tokens or replay of access tokens (from unauthorized parties) by requiring sender-constrained access tokens, either Mutual TLS for OAuth 2 or OAuth 2 Demonstration of Proof of Possession (DPoP).

- [ ] **V10.4.12** – Verify that for a given client, the authorization server only allows the 'response_mode' value that this client needs to use. For example, by having the authorization server validate this value against the expected values or by using pushed authorization request (PAR) or JWT-secured Authorization Request (JAR).

- [ ] **V10.4.14** – Verify that the authorization server issues only sender-constrained (Proof-of-Possession) access tokens, either with certificate-bound access tokens using mutual TLS (mTLS) or DPoP-bound access tokens (Demonstration of Proof of Possession).

- [ ] **V10.4.15** – Verify that, for a server-side client (which is not executed on the end-user device), the authorization server ensures that the 'authorization_details' parameter value is from the client backend and that the user has not tampered with it. For example, by requiring the usage of pushed authorization request (PAR) or JWT-secured Authorization Request (JAR).


🎯 **ASVS V11**

- [ ] **V11.2.5** – Verify that all cryptographic modules fail securely, and errors are handled in a way that does not enable vulnerabilities, such as Padding Oracle attacks.

- [ ] **V11.3.4** – Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair. The method of generation must be appropriate for the algorithm being used.


🎯 **ASVS V13**

- [ ] **V13.1.3** – Verify that the application documentation defines resource‑management strategies for every external system or service it uses (e.g., databases, file handles, threads, HTTP connections). This should include resource‑release procedures, timeout settings, failure handling, and where retry logic is implemented, specifying retry limits, delays, and back‑off algorithms. For synchronous HTTP request–response operations it should mandate short timeouts and either disable retries or strictly limit retries to prevent cascading delays and resource exhaustion.

- [ ] **V13.1.4** – Verify that the application's documentation defines the secrets that are critical for the security of the application and a schedule for rotating them, based on the organization's threat model and business requirements.

- [ ] **V13.4.6** – Verify that the application does not expose detailed version information of backend components.


🎯 **ASVS V14**

- [ ] **V14.2.5** – Verify that caching mechanisms are configured to only cache responses which have the expected content type for that resource and do not contain sensitive, dynamic content. The web server should return a 404 or 302 response when a non-existent file is accessed rather than returning a different, valid file. This should prevent Web Cache Deception attacks.


🎯 **ASVS V15**

- [ ] **V15.2.5** – Verify that the application implements additional protections around parts of the application which are documented as containing "dangerous functionality" or using third-party libraries considered to be "risky components". This could include techniques such as sandboxing, encapsulation, containerization or network level isolation to delay and deter attackers who compromise one part of an application from pivoting elsewhere in the application.

- [ ] **V15.4.3** – Verify that locks are used consistently to avoid threads getting stuck, whether by waiting on each other or retrying endlessly, and that locking logic stays within the code responsible for managing the resource to ensure locks cannot be inadvertently or maliciously modified by external classes or code.

- [ ] **V15.4.4** – Verify that resource allocation policies prevent thread starvation by ensuring fair access to resources, such as by leveraging thread pools, allowing lower-priority threads to proceed within a reasonable timeframe.


🎯 **ASVS V16**

- [ ] **V16.5.4** – Verify that a "last resort" error handler is defined which will catch all unhandled exceptions. This is both to avoid losing error details that must go to log files and to ensure that an error does not take down the entire application process, leading to a loss of availability.


🎯 **ASVS V17**

- [ ] **V17.2.8** – Verify that the Datagram Transport Layer Security (DTLS) certificate is checked against the Session Description Protocol (SDP) fingerprint attribute, terminating the media stream if the check fails, to ensure the authenticity of the media stream.


🎯 **ASVS V3**

- [ ] **V3.1.1** – Verify that application documentation states the expected security features that browsers using the application must support (such as HTTPS, HTTP Strict Transport Security (HSTS), Content Security Policy (CSP), and other relevant HTTP security mechanisms). It must also define how the application must behave when some of these features are not available (such as warning the user or blocking access).

- [ ] **V3.4.8** – Verify that all HTTP responses that initiate a document rendering (such as responses with Content-Type text/html), include the Cross‑Origin‑Opener‑Policy header field with the same-origin directive or the same-origin-allow-popups directive as required. This prevents attacks that abuse shared access to Window objects, such as tabnabbing and frame counting.

- [ ] **V3.7.4** – Verify that the application's top-level domain (e.g., site.tld) is added to the public preload list for HTTP Strict Transport Security (HSTS). This ensures that the use of TLS for the application is built directly into the main browsers, rather than relying only on the Strict-Transport-Security response header field.


🎯 **ASVS V4**

- [ ] **V4.2.4** – Verify that the application only accepts HTTP/2 and HTTP/3 requests where the header fields and values do not contain any CR (\r), LF (\n), or CRLF (\r\n) sequences, to prevent header injection attacks.


🎯 **ASVS V5**

- [ ] **V5.2.5** – Verify that the application does not allow uploading compressed files containing symlinks unless this is specifically required (in which case it will be necessary to enforce an allowlist of the files that can be symlinked to).


🎯 **ASVS V6**

- [ ] **V6.3.6** – Verify that email is not used as either a single-factor or multi-factor authentication mechanism.

- [ ] **V6.3.7** – Verify that users are notified after updates to authentication details, such as credential resets or modification of the username or email address.

- [ ] **V6.3.8** – Verify that valid users cannot be deduced from failed authentication challenges, such as by basing on error messages, HTTP response codes, or different response times. Registration and forgot password functionality must also have this protection.


🎯 **ASVS V8**

- [ ] **V8.1.3** – Verify that the application's documentation defines the environmental and contextual attributes (including but not limited to, time of day, user location, IP address, or device) that are used in the application to make security decisions, including those pertaining to authentication and authorization.

- [ ] **V8.3.2** – Verify that changes to values on which authorization decisions are made are applied immediately. Where changes cannot be applied immediately, (such as when relying on data in self-contained tokens), there must be mitigating controls to alert when a consumer performs an action when they are no longer authorized to do so and revert the change. Note that this alternative would not mitigate information leakage.

- [ ] **V8.3.3** – Verify that access to an object is based on the originating subject's (e.g. consumer's) permissions, not on the permissions of any intermediary or service acting on their behalf. For example, if a consumer calls a web service using a self-contained token for authentication, and the service then requests data from a different service, the second service will use the consumer's token, rather than a machine-to-machine token from the first service, to make permission decisions.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
