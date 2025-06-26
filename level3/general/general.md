# ASVS LEVEL3 Checklist – General – General

_Use during DESIGN and PRE-MERGE review._

- [ ] V1.3.12 – Verify that regular expressions are free from elements causing exponential backtracking, and ensure untrusted input is sanitized to mitigate ReDoS or Runaway Regex attacks.
- [ ] V1.5.3 – Verify that different parsers used in the application for the same data type (e.g., JSON parsers, XML parsers, URL parsers), perform parsing in a consistent way and use the same character encoding mechanism to avoid issues such as JSON Interoperability vulnerabilities or different URI or file parsing behavior being exploited in Remote File Inclusion (RFI) or Server-side Request Forgery (SSRF) attacks.
- [ ] V11.3.4 – Verify that nonces, initialization vectors, and other single-use numbers are not used for more than one encryption key and data-element pair. The method of generation must be appropriate for the algorithm being used.
- [ ] V11.3.5 – Verify that any combination of an encryption algorithm and a MAC algorithm is operating in encrypt-then-MAC mode.
- [ ] V11.7.1 – Verify that full memory encryption is in use that protects sensitive data while it is in use, preventing access by unauthorized users or processes.
- [ ] V11.7.2 – Verify that data minimization ensures the minimal amount of data is exposed during processing, and ensure that data is encrypted immediately after use or as soon as feasible.
- [ ] V12.1.5 – Verify that Encrypted Client Hello (ECH) is enabled in the application's TLS settings to prevent exposure of sensitive metadata, such as the Server Name Indication (SNI), during TLS handshake processes.
- [ ] V13.1.2 – Verify that for each service the application uses, the documentation defines the maximum number of concurrent connections (e.g., connection pool limits) and how the application behaves when that limit is reached, including any fallback or recovery mechanisms, to prevent denial of service conditions.
- [ ] V13.2.6 – Verify that where the application connects to separate services, it follows the documented configuration for each connection, such as maximum parallel connections, behavior when maximum allowed connections is reached, connection timeouts, and retry strategies.
- [ ] V13.3.4 – Verify that secrets are configured to expire and be rotated based on the application's documentation.
- [ ] V13.4.6 – Verify that the application does not expose detailed version information of backend components.
- [ ] V13.4.7 – Verify that the web tier is configured to only serve files with specific file extensions to prevent unintentional information, configuration, and source code leakage.
- [ ] V14.2.5 – Verify that caching mechanisms are configured to only cache responses which have the expected content type for that resource and do not contain sensitive, dynamic content. The web server should return a 404 or 302 response when a non-existent file is accessed rather than returning a different, valid file. This should prevent Web Cache Deception attacks.
- [ ] V14.2.8 – Verify that sensitive information is removed from the metadata of user-submitted files unless storage is consented to by the user.
- [ ] V15.1.5 – Verify that application documentation highlights parts of the application where "dangerous functionality" is being used.
- [ ] V15.4.1 – Verify that shared objects in multi-threaded code (such as caches, files, or in-memory objects accessed by multiple threads) are accessed safely by using thread-safe types and synchronization mechanisms like locks or semaphores to avoid race conditions and data corruption.
- [ ] V15.4.2 – Verify that checks on a resource's state, such as its existence or permissions, and the actions that depend on them are performed as a single atomic operation to prevent time-of-check to time-of-use (TOCTOU) race conditions. For example, checking if a file exists before opening it, or verifying a user’s access before granting it.
- [ ] V15.4.3 – Verify that locks are used consistently to avoid threads getting stuck, whether by waiting on each other or retrying endlessly, and that locking logic stays within the code responsible for managing the resource to ensure locks cannot be inadvertently or maliciously modified by external classes or code.
- [ ] V15.4.4 – Verify that resource allocation policies prevent thread starvation by ensuring fair access to resources, such as by leveraging thread pools, allowing lower-priority threads to proceed within a reasonable timeframe.
- [ ] V16.5.4 – Verify that a "last resort" error handler is defined which will catch all unhandled exceptions. This is both to avoid losing error details that must go to log files and to ensure that an error does not take down the entire application process, leading to a loss of availability.
- [ ] V17.1.2 – Verify that the Traversal Using Relays around NAT (TURN) service is not susceptible to resource exhaustion when legitimate users attempt to open a large number of ports on the TURN server.
- [ ] V17.2.5 – Verify that the media server is able to continue processing incoming media traffic during a flood of Secure Real-time Transport Protocol (SRTP) packets from legitimate users.
- [ ] V17.2.6 – Verify that the media server is not susceptible to the "ClientHello" Race Condition vulnerability in Datagram Transport Layer Security (DTLS) by checking if the media server is publicly known to be vulnerable or by performing the race condition test.
- [ ] V3.4.7 – Verify that the Content-Security-Policy header field specifies a location to report violations.
- [ ] V3.7.3 – Verify that the application shows a notification when the user is being redirected to a URL outside of the application's control, with an option to cancel the navigation.
- [ ] V4.1.5 – Verify that per-message digital signatures are used to provide additional assurance on top of transport protections for requests or transactions which are highly sensitive or which traverse a number of systems.
- [ ] V4.2.2 – Verify that when generating HTTP messages, the Content-Length header field does not conflict with the length of the content as determined by the framing of the HTTP protocol, in order to prevent request smuggling attacks.
- [ ] V4.2.3 – Verify that the application does not send nor accept HTTP/2 or HTTP/3 messages with connection-specific header fields such as Transfer-Encoding to prevent response splitting and header injection attacks.
- [ ] V4.2.4 – Verify that the application only accepts HTTP/2 and HTTP/3 requests where the header fields and values do not contain any CR (\r), LF (\n), or CRLF (\r\n) sequences, to prevent header injection attacks.
- [ ] V5.2.4 – Verify that a file size quota and maximum number of files per user are enforced to ensure that a single user cannot fill up the storage with too many files, or excessively large files.
- [ ] V5.2.6 – Verify that the application rejects uploaded images with a pixel size larger than the maximum allowed, to prevent pixel flood attacks.
- [ ] V5.3.3 – Verify that server-side file processing, such as file decompression, ignores user-provided path information to prevent vulnerabilities such as zip slip.
- [ ] V6.4.6 – Verify that administrative users can initiate the password reset process for the user, but that this does not allow them to change or choose the user's password. This prevents a situation where they know the user's password.
- [ ] V6.5.8 – Verify that time-based one-time passwords (TOTPs) are checked based on a time source from a trusted service and not from an untrusted or client provided time.
