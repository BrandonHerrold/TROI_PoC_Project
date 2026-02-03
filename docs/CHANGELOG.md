
---

# 🧾 CHANGELOG.md

```markdown
# Changelog
All notable changes to this project are documented here.

The format follows a simplified version of:
https://keepachangelog.com/

---

## [Unreleased]
- Phase 2.1 — Warehouse Inventory View (in progress)

---

## [0.3.0] — 2026-02-02
### Added
- Forced logout on server restart using nonce-based middleware
- 15-minute inactivity session timeout
- Client-side idle warning and auto-logout
- Protected site homepage (`/`)
- Base template with session-timeout UX

### Fixed
- Session persistence after server restart
- Admin auto-login confusion clarified and resolved
- Middleware return path bugs (NoneType responses)

---

## [0.2.0] — 2026-02-01
### Added
- Ledger-derived on-hand inventory helper
- Services layer for inventory math
- Validation of RECEIVE / ISSUE semantics
- Realistic warehouse inventory calculations

### Fixed
- Negative inventory caused by incorrect RECEIVE modeling

---

## [0.1.0] — 2026-01-31
### Added
- Initial Django project setup
- Parts catalog with image uploads
- Media configuration
- Django Admin customization
- Inventory ledger models
- Location modeling (warehouse + technicians)

---

## Notes
- SQLite used intentionally for PoC simplicity
- Inventory quantities are never stored directly
- All inventory state is derived from history
