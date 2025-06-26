# ASVS 2 Checklist 🟡 – General – Api

_Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility._

- [ ] 🟡 V1.1.2 – Verify that the application performs output encoding and escaping either as a final step before being used by the interpreter for which it is intended or by the interpreter itself.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V1.5.2 – Verify that deserialization of untrusted data enforces safe input handling, such as using an allowlist of object types or restricting client-defined object types, to prevent deserialization attacks. Deserialization mechanisms that are explicitly defined as insecure must not be used with untrusted input.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V3.5.4 – Verify that separate applications are hosted on different hostnames to leverage the restrictions provided by same-origin policy, including how documents or scripts loaded by one origin can interact with resources from another origin and hostname-based restrictions on cookies.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V4.1.2 – Verify that only user-facing endpoints (intended for manual web-browser access) automatically redirect from HTTP to HTTPS, while other services or endpoints do not implement transparent redirects. This is to avoid a situation where a client is erroneously sending unencrypted HTTP requests, but since the requests are being automatically redirected to HTTPS, the leakage of sensitive data goes undiscovered.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V4.3.1 – Verify that a query allowlist, depth limiting, amount limiting, or query cost analysis is used to prevent GraphQL or data layer expression Denial of Service (DoS) as a result of expensive, nested queries.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V4.3.2 – Verify that GraphQL introspection queries are disabled in the production environment unless the GraphQL API is meant to be used by other parties.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V4.4.2 – Verify that, during the initial HTTP WebSocket handshake, the Origin header field is checked against a list of origins allowed for the application.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V4.4.4 – Verify that dedicated WebSocket session management tokens are initially obtained or validated through the previously authenticated HTTPS session when transitioning an existing HTTPS session to a WebSocket channel.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V5.4.1 – Verify that the application validates or ignores user-submitted filenames, including in a JSON, JSONP, or URL parameter and specifies a filename in the Content-Disposition header field in the response.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V6.6.3 – Verify that a code based out-of-band authentication mechanism is protected against brute force attacks by using rate limiting. Consider also using a code with at least 64 bits of entropy.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V8.1.2 – Verify that authorization documentation defines rules for field-level access restrictions (both read and write) based on consumer permissions and resource attributes. Note that these rules might depend on other attribute values of the relevant data object, such as state or status.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V8.2.3 – Verify that the application ensures that field-level access is restricted to consumers with explicit permissions to specific fields to mitigate broken object property level authorization (BOPLA).
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V9.2.4 – Verify that, if a token issuer uses the same private key for issuing tokens to different audiences, the issued tokens contain an audience restriction that uniquely identifies the intended audiences. This will prevent a token from being reused with an unintended audience. If the audience identifier is dynamically provisioned, the token issuer must validate these audiences in order to make sure that they do not result in audience impersonation.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V10.3.1 – Verify that the resource server only accepts access tokens that are intended for use with that service (audience). The audience may be included in a structured access token (such as the 'aud' claim in JWT), or it can be checked using the token introspection endpoint.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V12.3.1 – Verify that an encrypted protocol such as TLS is used for all inbound and outbound connections to and from the application, including monitoring systems, management tools, remote access and SSH, middleware, databases, mainframes, partner systems, or external APIs. The server must not fall back to insecure or unencrypted protocols.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V13.2.1 – Verify that communications between backend application components that don't support the application's standard user session mechanism, including APIs, middleware, and data layers, are authenticated. Authentication must use individual service accounts, short-term tokens, or certificate-based authentication and not unchanging credentials such as passwords, API keys, or shared accounts with privileged access.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V13.2.2 – Verify that communications between backend application components, including local or operating system services, APIs, middleware, and data layers, are performed with accounts assigned the least necessary privileges.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V13.3.1 – Verify that a secrets management solution, such as a key vault, is used to securely create, store, control access to, and destroy backend secrets. These could include passwords, key material, integrations with databases and third-party systems, keys and seeds for time-based tokens, other internal secrets, and API keys. Secrets must not be included in application source code or included in build artifacts. For an L3 application, this must involve a hardware-backed solution such as an HSM.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V13.4.5 – Verify that documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V14.1.1 – Verify that all sensitive data created and processed by the application has been identified and classified into protection levels. This includes data that is only encoded and therefore easily decoded, such as Base64 strings or the plaintext payload inside a JWT. Protection levels need to take into account any data protection and privacy regulations and standards which the application is required to comply with.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V15.3.4 – Verify that all proxying and middleware components transfer the user's original IP address correctly using trusted data fields that cannot be manipulated by the end user, and the application and web server use this correct value for logging and security decisions such as rate limiting, taking into account that even the original IP address may not be reliable due to dynamic IPs, VPNs, or corporate firewalls.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟡 V17.3.1 – Verify that the signaling server is able to continue processing legitimate incoming signaling messages during a flood attack. This should be achieved by implementing rate limiting at the signaling level.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
