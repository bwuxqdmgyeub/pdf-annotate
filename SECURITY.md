# Security Policy

## Supported versions

| Version | Supported |
|---------|-----------|
| 0.6.x   | yes       |
| < 0.6   | no        |

## Reporting a vulnerability

The PDF Editor parses untrusted PDF files, so we take parser and plugin
sandbox issues seriously. Please **do not** open a public issue for:

- crashes or memory corruption triggered by a crafted PDF
- path traversal in the recent-files store
- plugin loading from a user-writable directory without confirmation
- signature verification bypasses

Instead, email `security@pdf-annotate.dev` with a minimal reproducer
PDF (or a hash + generation script) and the affected version. We aim to
acknowledge within 72 hours and ship a fix in the next patch release.

## Scope

In scope: the core host, the plugin loader, the document model, and the
bundled extensions under `src/pdf_annotate/extensions/`.

Out of scope: third-party plugins published outside this repository,
and issues that require the attacker to already control the user's
account.