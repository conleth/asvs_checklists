# ASVS 3 Checklist – Javascript – Integration

_Use during DESIGN and PRE-MERGE review. This list is tailored to your stack and responsibility._

- [ ] V3.6.1 – Verify that client-side assets, such as JavaScript libraries, CSS, or web fonts, are only hosted externally (e.g., on a Content Delivery Network) if the resource is static and versioned and Subresource Integrity (SRI) is used to validate the integrity of the asset. If this is not possible, there should be a documented security decision to justify this for each resource.
