# ASVS 2 Checklist – General – Observability

_Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility._

- [ ] V12.3.1 – Verify that an encrypted protocol such as TLS is used for all inbound and outbound connections to and from the application, including monitoring systems, management tools, remote access and SSH, middleware, databases, mainframes, partner systems, or external APIs. The server must not fall back to insecure or unencrypted protocols.
- [ ] V13.4.4 – Verify that using the HTTP TRACE method is not supported in production environments, to avoid potential information leakage.
- [ ] V13.4.5 – Verify that documentation (such as for internal APIs) and monitoring endpoints are not exposed unless explicitly intended.
- [ ] V15.3.4 – Verify that all proxying and middleware components transfer the user's original IP address correctly using trusted data fields that cannot be manipulated by the end user, and the application and web server use this correct value for logging and security decisions such as rate limiting, taking into account that even the original IP address may not be reliable due to dynamic IPs, VPNs, or corporate firewalls.
- [ ] V16.1.1 – Verify that an inventory exists documenting the logging performed at each layer of the application's technology stack, what events are being logged, log formats, where that logging is stored, how it is used, how access to it is controlled, and for how long logs are kept.
- [ ] V16.2.2 – Verify that time sources for all logging components are synchronized, and that timestamps in security event metadata use UTC or include an explicit time zone offset. UTC is recommended to ensure consistency across distributed systems and to prevent confusion during daylight saving time transitions.
- [ ] V16.2.4 – Verify that logs can be read and correlated by the log processor that is in use, preferably by using a common logging format.
- [ ] V16.2.5 – Verify that when logging sensitive data, the application enforces logging based on the data's protection level. For example, it may not be allowed to log certain data, such as credentials or payment details. Other data, such as session tokens, may only be logged by being hashed or masked, either in full or partially.
- [ ] V16.3.2 – Verify that failed authorization attempts are logged. For L3, this must include logging all authorization decisions, including logging when sensitive data is accessed (without logging the sensitive data itself).
- [ ] V16.4.1 – Verify that all logging components appropriately encode data to prevent log injection.
- [ ] V16.4.3 – Verify that logs are securely transmitted to a logically separate system for analysis, detection, alerting, and escalation. The aim is to ensure that if the application is breached, the logs are not compromised.
- [ ] V16.5.1 – Verify that a generic message is returned to the consumer when an unexpected or security-sensitive error occurs, ensuring no exposure of sensitive internal system data such as stack traces, queries, secret keys, and tokens.
