# ASVS 3 Checklist 🔴 – General – General

_Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility._

- [ ] 🔴 V1.3.12 – Verify that regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V3.4.7 – Verify that the Content-Security-Policy header field specifies a location to report violations.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V3.7.3 – Verify that the application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V4.1.5 – Verify that per-message digital signatures are used to provide additional assurance on top of transport protections for requests or transactions which are highly sensitive or which traverse a number of systems.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V4.2.2 – Verify that when generating HTTP messages, the Content-Length header field does not conflict with the length of the content as determined by the framing of the HTTP protocol, in order to prevent request smuggling attacks.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V4.2.3 – Verify that the application does not send nor accept HTTP/2 or HTTP/3 messages with connection-specific header fields such as Transfer-Encoding to prevent response splitting and header injection attacks.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V5.2.4 – Verify that a file size quota and maximum number of files per user are enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V5.2.6 – Verify that the application rejects uploaded images with a pixel size larger than the maximum allowed, to prevent pixel flood attacks.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V6.4.6 – Verify that administrative users can initiate the password reset process for the user, but that this does not allow them to change or choose the user's password. This prevents a situation where they know the user's password.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V11.7.2 – Verify that data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V13.2.6 – Verify that where the application connects to separate services, it follows the documented configuration for each connection, such as maximum parallel connections, behavior when maximum allowed connections is reached, connection timeouts, and retry strategies.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V15.4.1 – Verify that shared objects in multi-threaded code (such as caches, files, or in-memory objects accessed by multiple threads) are accessed safely by using thread-safe types and synchronization mechanisms like locks or semaphores to avoid race conditions and data corruption.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V17.1.2 – Verify that the Traversal Using Relays around NAT (TURN) service is not susceptible to resource exhaustion when legitimate users attempt to open a large number of ports on the TURN server.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🔴 V17.2.5 – Verify that the media server is able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
