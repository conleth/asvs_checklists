🟡 **Level 2**

# ASVS 2 Checklist – general – backend

*Use during **DESIGN** and **PRE‑MERGE** review. This list is tailored to your stack and responsibility.*



🎯 **ASVS V1**

- [ ] **V1.1.1** – Verify that input is decoded or unescaped into a canonical form only once, it is only decoded when encoded data in that form is expected, and that this is done before processing the input further, for example it is not performed after input validation or sanitization.

- [ ] **V1.1.2** – Verify that the application performs output encoding and escaping either as a final step before being used by the interpreter for which it is intended or by the interpreter itself.

- [ ] **V1.3.10** – Verify that format strings which might resolve in an unexpected or malicious way when used are sanitized before being processed.

- [ ] **V1.4.2** – Verify that sign, range, and input validation techniques are used to prevent integer overflows.


🎯 **ASVS V10**

- [ ] **V10.1.2** – Verify that the client only accepts values from the authorization server (such as the authorization code or ID Token) if these values result from an authorization flow that was initiated by the same user agent session and transaction. This requires that client-generated secrets, such as the proof key for code exchange (PKCE) 'code_verifier', 'state' or OIDC 'nonce', are not guessable, are specific to the transaction, and are securely bound to both the client and the user agent session in which the transaction was started.

- [ ] **V10.2.1** – Verify that, if the code flow is used, the OAuth client has protection against browser-based request forgery attacks, commonly known as cross-site request forgery (CSRF), which trigger token requests, either by using proof key for code exchange (PKCE) functionality or checking the 'state' parameter that was sent in the authorization request.

- [ ] **V10.2.2** – Verify that, if the OAuth client can interact with more than one authorization server, it has a defense against mix-up attacks. For example, it could require that the authorization server return the 'iss' parameter value and validate it in the authorization response and the token response.

- [ ] **V10.3.2** – Verify that the resource server enforces authorization decisions based on claims from the access token that define delegated authorization. If claims such as 'sub', 'scope', and 'authorization_details' are present, they must be part of the decision.

- [ ] **V10.3.4** – Verify that, if the resource server requires specific authentication strength, methods, or recentness, it verifies that the presented access token satisfies these constraints. For example, if present, using the OIDC 'acr', 'amr' and 'auth_time' claims respectively.

- [ ] **V10.4.10** – Verify that confidential client is authenticated for client-to-authorized server backchannel requests such as token requests, pushed authorization requests (PAR), and token revocation requests.

- [ ] **V10.4.11** – Verify that the authorization server configuration only assigns the required scopes to the OAuth client.

- [ ] **V10.4.6** – Verify that, if the code grant is used, the authorization server mitigates authorization code interception attacks by requiring proof key for code exchange (PKCE). For authorization requests, the authorization server must require a valid 'code_challenge' value and must not accept a 'code_challenge_method' value of 'plain'. For a token request, it must require validation of the 'code_verifier' parameter.

- [ ] **V10.4.7** – Verify that if the authorization server supports unauthenticated dynamic client registration, it mitigates the risk of malicious client applications. It must validate client metadata such as any registered URIs, ensure the user's consent, and warn the user before processing an authorization request with an untrusted client application.

- [ ] **V10.4.9** – Verify that refresh tokens and reference access tokens can be revoked by an authorized user using the authorization server user interface, to mitigate the risk of malicious clients or stolen tokens.

- [ ] **V10.5.1** – Verify that the client (as the relying party) mitigates ID Token replay attacks. For example, by ensuring that the 'nonce' claim in the ID Token matches the 'nonce' value sent in the authentication request to the OpenID Provider (in OAuth2 refereed to as the authorization request sent to the authorization server).

- [ ] **V10.5.3** – Verify that the client rejects attempts by a malicious authorization server to impersonate another authorization server through authorization server metadata. The client must reject authorization server metadata if the issuer URL in the authorization server metadata does not exactly match the pre-configured issuer URL expected by the client.

- [ ] **V10.7.1** – Verify that the authorization server ensures that the user consents to each authorization request. If the identity of the client cannot be assured, the authorization server must always explicitly prompt the user for consent.

- [ ] **V10.7.2** – Verify that when the authorization server prompts for user consent, it presents sufficient and clear information about what is being consented to. When applicable, this should include the nature of the requested authorizations (typically based on scope, resource server, Rich Authorization Requests (RAR) authorization details), the identity of the authorized application, and the lifetime of these authorizations.

- [ ] **V10.7.3** – Verify that the user can review, modify, and revoke consents which the user has granted through the authorization server.


🎯 **ASVS V11**

- [ ] **V11.1.1** – Verify that there is a documented policy for management of cryptographic keys and a cryptographic key lifecycle that follows a key management standard such as NIST SP 800-57. This should include ensuring that keys are not overshared (for example, with more than two entities for shared secrets and more than one entity for private keys).

- [ ] **V11.1.2** – Verify that a cryptographic inventory is performed, maintained, regularly updated, and includes all cryptographic keys, algorithms, and certificates used by the application. It must also document where keys can and cannot be used in the system, and the types of data that can and cannot be protected using the keys.

- [ ] **V11.2.1** – Verify that industry-validated implementations (including libraries and hardware-accelerated implementations) are used for cryptographic operations.

- [ ] **V11.2.2** – Verify that the application is designed with crypto agility such that random number, authenticated encryption, MAC, or hashing algorithms, key lengths, rounds, ciphers and modes can be reconfigured, upgraded, or swapped at any time, to protect against cryptographic breaks. Similarly, it must also be possible to replace keys and passwords and re-encrypt data. This will allow for seamless upgrades to post-quantum cryptography (PQC), once high-assurance implementations of approved PQC schemes or standards are widely available.

- [ ] **V11.2.3** – Verify that all cryptographic primitives utilize a minimum of 128-bits of security based on the algorithm, key size, and configuration. For example, a 256-bit ECC key provides roughly 128 bits of security where RSA requires a 3072-bit key to achieve 128 bits of security.

- [ ] **V11.3.3** – Verify that encrypted data is protected against unauthorized modification preferably by using an approved authenticated encryption method or by combining an approved encryption method with an approved MAC algorithm.

- [ ] **V11.4.2** – Verify that passwords are stored using an approved, computationally intensive, key derivation function (also known as a "password hashing function"), with parameter settings configured based on current guidance. The settings should balance security and performance to make brute-force attacks sufficiently challenging for the required level of security.

- [ ] **V11.4.3** – Verify that hash functions used in digital signatures, as part of data authentication or data integrity are collision resistant and have appropriate bit-lengths. If collision resistance is required, the output length must be at least 256 bits. If only resistance to second pre-image attacks is required, the output length must be at least 128 bits.

- [ ] **V11.4.4** – Verify that the application uses approved key derivation functions with key stretching parameters when deriving secret keys from passwords. The parameters in use must balance security and performance to prevent brute-force attacks from compromising the resulting cryptographic key.

- [ ] **V11.5.1** – Verify that all random numbers and strings which are intended to be non-guessable must be generated using a cryptographically secure pseudo-random number generator (CSPRNG) and have at least 128 bits of entropy. Note that UUIDs do not respect this condition.

- [ ] **V11.6.1** – Verify that only approved cryptographic algorithms and modes of operation are used for key generation and seeding, and digital signature generation and verification. Key generation algorithms must not generate insecure keys vulnerable to known attacks, for example, RSA keys which are vulnerable to Fermat factorization.


🎯 **ASVS V12**

- [ ] **V12.1.3** – Verify that the application validates that mTLS client certificates are trusted before using the certificate identity for authentication or authorization.

- [ ] **V12.3.1** – Verify that an encrypted protocol such as TLS is used for all inbound and outbound connections to and from the application, including monitoring systems, management tools, remote access and SSH, middleware, databases, mainframes, partner systems, or external APIs. The server must not fall back to insecure or unencrypted protocols.


🎯 **ASVS V13**

- [ ] **V13.2.1** – Verify that communications between backend application components that don't support the application's standard user session mechanism, including APIs, middleware, and data layers, are authenticated. Authentication must use individual service accounts, short-term tokens, or certificate-based authentication and not unchanging credentials such as passwords, API keys, or shared accounts with privileged access.

- [ ] **V13.2.2** – Verify that communications between backend application components, including local or operating system services, APIs, middleware, and data layers, are performed with accounts assigned the least necessary privileges.

- [ ] **V13.2.3** – Verify that if a credential has to be used for service authentication, the credential being used by the consumer is not a default credential (e.g., root/root or admin/admin).

- [ ] **V13.3.1** – Verify that a secrets management solution, such as a key vault, is used to securely create, store, control access to, and destroy backend secrets. These could include passwords, key material, integrations with databases and third-party systems, keys and seeds for time-based tokens, other internal secrets, and API keys. Secrets must not be included in application source code or included in build artifacts. For an L3 application, this must involve a hardware-backed solution such as an HSM.

- [ ] **V13.4.2** – Verify that debug modes are disabled for all components in production environments to prevent exposure of debugging features and information leakage.

- [ ] **V13.4.4** – Verify that using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage.


🎯 **ASVS V14**

- [ ] **V14.1.2** – Verify that all sensitive data protection levels have a documented set of protection requirements. This must include (but not be limited to) requirements related to general encryption, integrity verification, retention, how the data is to be logged, access controls around sensitive data in logs, database-level encryption, privacy and privacy-enhancing technologies to be used, and other confidentiality requirements.

- [ ] **V14.3.3** – Verify that data stored in browser storage (such as localStorage, sessionStorage, IndexedDB, or cookies) does not contain sensitive data, with the exception of session tokens.


🎯 **ASVS V15**

- [ ] **V15.3.5** – Verify that the application explicitly ensures that variables are of the correct type and performs strict equality and comparator operations. This is to avoid type juggling or type confusion vulnerabilities caused by the application code making an assumption about a variable type.


🎯 **ASVS V16**

- [ ] **V16.1.1** – Verify that an inventory exists documenting the logging performed at each layer of the application's technology stack, what events are being logged, log formats, where that logging is stored, how it is used, how access to it is controlled, and for how long logs are kept.

- [ ] **V16.2.4** – Verify that logs can be read and correlated by the log processor that is in use, preferably by using a common logging format.

- [ ] **V16.2.5** – Verify that when logging sensitive data, the application enforces logging based on the data's protection level. For example, it may not be allowed to log certain data, such as credentials or payment details. Other data, such as session tokens, may only be logged by being hashed or masked, either in full or partially.

- [ ] **V16.3.1** – Verify that all authentication operations are logged, including successful and unsuccessful attempts. Additional metadata, such as the type of authentication or factors used, should also be collected.

- [ ] **V16.3.2** – Verify that failed authorization attempts are logged. For L3, this must include logging all authorization decisions, including logging when sensitive data is accessed (without logging the sensitive data itself).

- [ ] **V16.3.3** – Verify that the application logs the security events that are defined in the documentation and also logs attempts to bypass the security controls, such as input validation, business logic, and anti-automation.

- [ ] **V16.4.2** – Verify that logs are protected from unauthorized access and cannot be modified.

- [ ] **V16.5.3** – Verify that the application fails gracefully and securely, including when an exception occurs, preventing fail-open conditions such as processing a transaction despite errors resulting from validation logic.


🎯 **ASVS V17**

- [ ] **V17.2.1** – Verify that the key for the Datagram Transport Layer Security (DTLS) certificate is managed and protected based on the documented policy for management of cryptographic keys.

- [ ] **V17.2.3** – Verify that Secure Real-time Transport Protocol (SRTP) authentication is checked at the media server to prevent Real-time Transport Protocol (RTP) injection attacks from leading to either a Denial of Service condition or audio or video media insertion into media streams.

- [ ] **V17.2.4** – Verify that the media server is able to continue processing incoming media traffic when encountering malformed Secure Real-time Transport Protocol (SRTP) packets.

- [ ] **V17.3.2** – Verify that the signaling server is able to continue processing legitimate signaling messages when encountering malformed signaling message that could cause a denial of service condition. This could include implementing input validation, safely handling integer overflows, preventing buffer overflows, and employing other robust error-handling techniques.


🎯 **ASVS V2**

- [ ] **V2.1.3** – Verify that expectations for business logic limits and validations are documented, including both per-user and globally across the application.


🎯 **ASVS V3**

- [ ] **V3.3.4** – Verify that if the value of a cookie is not meant to be accessible to client-side scripts (such as a session token), the cookie must have the 'HttpOnly' attribute set and the same value (e. g. session token) must only be transferred to the client via the 'Set-Cookie' header field.


🎯 **ASVS V4**

- [ ] **V4.4.3** – Verify that, if the application's standard session management cannot be used, dedicated tokens are being used for this, which comply with the relevant Session Management security requirements.

- [ ] **V4.4.4** – Verify that dedicated WebSocket session management tokens are initially obtained or validated through the previously authenticated HTTPS session when transitioning an existing HTTPS session to a WebSocket channel.


🎯 **ASVS V6**

- [ ] **V6.1.3** – Verify that, if the application includes multiple authentication pathways, these are all documented together with the security controls and authentication strength which must be consistently enforced across them.

- [ ] **V6.3.3** – Verify that either a multi-factor authentication mechanism or a combination of single-factor authentication mechanisms, must be used in order to access the application. For L3, one of the factors must be a hardware-based authentication mechanism which provides compromise and impersonation resistance against phishing attacks while verifying the intent to authenticate by requiring a user-initiated action (such as a button press on a FIDO hardware key or a mobile phone). Relaxing any of the considerations in this requirement requires a fully documented rationale and a comprehensive set of mitigating controls.

- [ ] **V6.3.4** – Verify that, if the application includes multiple authentication pathways, there are no undocumented pathways and that security controls and authentication strength are enforced consistently.

- [ ] **V6.4.3** – Verify that a secure process for resetting a forgotten password is implemented, that does not bypass any enabled multi-factor authentication mechanisms.

- [ ] **V6.4.4** – Verify that if a multi-factor authentication factor is lost, evidence of identity proofing is performed at the same level as during enrollment.

- [ ] **V6.5.1** – Verify that lookup secrets, out-of-band authentication requests or codes, and time-based one-time passwords (TOTPs) are only successfully usable once.

- [ ] **V6.5.3** – Verify that lookup secrets, out-of-band authentication code, and time-based one-time password seeds, are generated using a Cryptographically Secure Pseudorandom Number Generator (CSPRNG) to avoid predictable values.

- [ ] **V6.5.4** – Verify that lookup secrets and out-of-band authentication codes have a minimum of 20 bits of entropy (typically 4 random alphanumeric characters or 6 random digits is sufficient).

- [ ] **V6.5.5** – Verify that out-of-band authentication requests, codes, or tokens, as well as time-based one-time passwords (TOTPs) have a defined lifetime. Out of band requests must have a maximum lifetime of 10 minutes and for TOTP a maximum lifetime of 30 seconds.

- [ ] **V6.6.1** – Verify that authentication mechanisms using the Public Switched Telephone Network (PSTN) to deliver One-time Passwords (OTPs) via phone or SMS are offered only when the phone number has previously been validated, alternate stronger methods (such as Time based One-time Passwords) are also offered, and the service provides information on their security risks to users. For L3 applications, phone and SMS must not be available as options.

- [ ] **V6.6.2** – Verify that out-of-band authentication requests, codes, or tokens are bound to the original authentication request for which they were generated and are not usable for a previous or subsequent one.

- [ ] **V6.6.3** – Verify that a code based out-of-band authentication mechanism is protected against brute force attacks by using rate limiting. Consider also using a code with at least 64 bits of entropy.

- [ ] **V6.8.2** – Verify that the presence and integrity of digital signatures on authentication assertions (for example on JWTs or SAML assertions) are always validated, rejecting any assertions that are unsigned or have invalid signatures.

- [ ] **V6.8.4** – Verify that, if an application uses a separate Identity Provider (IdP) and expects specific authentication strength, methods, or recentness for specific functions, the application verifies this using the information returned by the IdP. For example, if OIDC is used, this might be achieved by validating ID Token claims such as 'acr', 'amr', and 'auth_time' (if present). If the IdP does not provide this information, the application must have a documented fallback approach that assumes that the minimum strength authentication mechanism was used (for example, single-factor authentication using username and password).


🎯 **ASVS V7**

- [ ] **V7.1.1** – Verify that the user's session inactivity timeout and absolute maximum session lifetime are documented, are appropriate in combination with other controls, and that the documentation includes justification for any deviations from NIST SP 800-63B re-authentication requirements.

- [ ] **V7.1.2** – Verify that the documentation defines how many concurrent (parallel) sessions are allowed for one account as well as the intended behaviors and actions to be taken when the maximum number of active sessions is reached.

- [ ] **V7.1.3** – Verify that all systems that create and manage user sessions as part of a federated identity management ecosystem (such as SSO systems) are documented along with controls to coordinate session lifetimes, termination, and any other conditions that require re-authentication.

- [ ] **V7.3.1** – Verify that there is an inactivity timeout such that re-authentication is enforced according to risk analysis and documented security decisions.

- [ ] **V7.3.2** – Verify that there is an absolute maximum session lifetime such that re-authentication is enforced according to risk analysis and documented security decisions.

- [ ] **V7.4.3** – Verify that the application gives the option to terminate all other active sessions after a successful change or removal of any authentication factor (including password change via reset or recovery and, if present, an MFA settings update).

- [ ] **V7.4.4** – Verify that all pages that require authentication have easy and visible access to logout functionality.

- [ ] **V7.4.5** – Verify that application administrators are able to terminate active sessions for an individual user or for all users.

- [ ] **V7.5.1** – Verify that the application requires full re-authentication before allowing modifications to sensitive account attributes which may affect authentication such as email address, phone number, MFA configuration, or other information used in account recovery.

- [ ] **V7.5.2** – Verify that users are able to view and (having authenticated again with at least one factor) terminate any or all currently active sessions.

- [ ] **V7.6.1** – Verify that session lifetime and termination between Relying Parties (RPs) and Identity Providers (IdPs) behave as documented, requiring re-authentication as necessary such as when the maximum time between IdP authentication events is reached.

- [ ] **V7.6.2** – Verify that creation of a session requires either the user's consent or an explicit action, preventing the creation of new application sessions without user interaction.


🎯 **ASVS V8**

- [ ] **V8.1.2** – Verify that authorization documentation defines rules for field-level access restrictions (both read and write) based on consumer permissions and resource attributes. Note that these rules might depend on other attribute values of the relevant data object, such as state or status.

- [ ] **V8.2.3** – Verify that the application ensures that field-level access is restricted to consumers with explicit permissions to specific fields to mitigate broken object property level authorization (BOPLA).


🎯 **ASVS V9**

- [ ] **V9.2.2** – Verify that the service receiving a token validates the token to be the correct type and is meant for the intended purpose before accepting the token's contents. For example, only access tokens can be accepted for authorization decisions and only ID Tokens can be used for proving user authentication.

<details><summary>Advanced defense‑in‑depth guidance</summary>


_Add organisation‑specific recommendations, links to tooling, threat models, etc._

</details>


---

Generated from [OWASP ASVS 5.0.0](https://owasp.org/www-project-application-security-verification-standard/) on {}. Do not edit manually; run `update_checklists.py` instead.
