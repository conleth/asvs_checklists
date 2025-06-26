# ASVS 1 Checklist 🟢 – Javascript – Frontend

_Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility._

- [ ] 🟢 V1.2.2 – Verify that when dynamically building URLs, untrusted data is encoded according to its context (e.g., URL encoding or base64url encoding for query or path parameters). Ensure that only safe URL protocols are permitted (e.g., disallow javascript: or data:).
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟢 V1.2.3 – Verify that output encoding or escaping is used when dynamically building JavaScript content (including JSON), to avoid changing the message or document structure (to avoid JavaScript and JSON injection).
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟢 V3.2.2 – Verify that content intended to be displayed as text, rather than rendered as HTML, is handled using safe rendering functions (such as createTextNode or textContent) to prevent unintended execution of content such as HTML or JavaScript.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
- [ ] 🟢 V8.3.1 – Verify that the application enforces authorization rules at a trusted service layer and doesn't rely on controls that an untrusted consumer could manipulate, such as client-side JavaScript.
  <details>
<summary>Advanced: Defense-in-Depth Guidance</summary>

_No additional guidance provided._

</details>
