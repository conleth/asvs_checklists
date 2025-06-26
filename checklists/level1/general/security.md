# ASVS 1 Checklist 🟢 – General – Security

_Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility._

- [ ] 🟢 V6.4.1 – Verify that system generated initial passwords or activation codes are securely randomly generated, follow the existing password policy, and expire after a short period of time or after they are initially used. These initial secrets must not be permitted to become the long term password.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟢 V7.2.2 – Verify that the application uses either self-contained or reference tokens that are dynamically generated for session management, i.e. not using static API secrets and keys.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟢 V7.2.3 – Verify that if reference tokens are used to represent user sessions, they are unique and generated using a cryptographically secure pseudo-random number generator (CSPRNG) and possess at least 128 bits of entropy.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟢 V9.1.3 – Verify that key material that is used to validate self-contained tokens is from trusted pre-configured sources for the token issuer, preventing attackers from specifying untrusted sources and keys. For JWTs and other JWS structures, headers such as 'jku', 'x5u', and 'jwk' must be validated against an allowlist of trusted sources.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟢 V9.2.1 – Verify that, if a validity time span is present in the token data, the token and its content are accepted only if the verification time is within this validity time span. For example, for JWTs, the claims 'nbf' and 'exp' must be verified.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟢 V11.4.1 – Verify that only approved hash functions are used for general cryptographic use cases, including digital signatures, HMAC, KDF, and random bit generation. Disallowed hash functions, such as MD5, must not be used for any cryptographic purpose.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
