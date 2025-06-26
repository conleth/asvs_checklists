# ASVS 3 Checklist – Java – Backend

_Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility._

- [ ] V3.2.3 – Verify that the application avoids DOM clobbering when using client-side JavaScript by employing explicit variable declarations, performing strict type checking, avoiding storing global variables on the document object, and implementing namespace isolation.
- [ ] V3.5.7 – Verify that data requiring authorization is not included in script resource responses, like JavaScript files, to prevent Cross-Site Script Inclusion (XSSI) attacks.
