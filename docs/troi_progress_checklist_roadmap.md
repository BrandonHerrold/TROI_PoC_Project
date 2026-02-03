# G-PIT — Progress Checklist & Roadmap

> **Project:** G-PIT (Generic Parts Inventory for Technicians)
>
> **Purpose:** Time-bound, non-prod Proof of Concept demonstrating a safe, auditable parts inventory system for technicians.
> 
> **Status:** Core foundations complete; ready for feature expansion and GitHub publication.

---

## ✅ Completed (Foundational Milestones)

### Repository & Environment
- [x] Created project workspace (`troi-poc`)
- [x] Initialized Git repository
- [x] Added `.gitignore` (excluded `.venv/`, `.vs/`, `db.sqlite3`, logs)
- [x] Created and activated Python virtual environment
- [x] Installed Django in venv
- [x] Established rule: run all Django commands from `app/`

### Django Project Setup
- [x] Created Django project (`troi`)
- [x] Verified local server startup (`runserver --noreload`)
- [x] Created admin superuser
- [x] Verified access to Django Admin UI

---

## 📦 Parts Catalog (App: `parts`)

- [x] Created Django app `parts`
- [x] Added app to `INSTALLED_APPS`
- [x] Implemented `Part` model:
  - `part_number` (unique identifier)
  - `name`, `description`
  - `unit` (each / roll / box)
  - `is_active`
  - timestamps (`created_at`, `updated_at`)
- [x] Created and applied migrations
- [x] Registered `Part` model in Django Admin
- [x] Verified add/edit/search of parts in Admin UI
- [x] Added sample parts for testing/demo

---

## 🏭 Stock & Inventory Ledger (App: `stock`)

### Models
- [x] Created Django app `stock`
- [x] Added app to `INSTALLED_APPS`
- [x] Implemented core inventory models:

#### `Location`
- Warehouse / Technician / Other
- Active flag
- Optional owner user

#### `InventoryLedger`
- Actions: RECEIVE / ISSUE / TRANSFER / ADJUST
- Actor (user)
- From / To locations
- Reference + notes
- Timestamp

#### `InventoryLedgerItem`
- Ledger line items (Part + Quantity)

### Admin
- [x] Registered `Location` in Admin
- [x] Registered `InventoryLedger` with inline `InventoryLedgerItem`
- [x] Verified creation of ledger entries via Admin UI

### System Concepts Implemented
- [x] Append-only inventory history (audit-friendly)
- [x] Inventory movements tracked via ledger, not stored counts

---

## 🧠 Key Engineering Lessons Learned

- PowerShell ISE is unsuitable for Django dev servers (signal handling issues)
- Use VS Code / standard terminal instead
- Django Admin auto-imports all `admin.py` files → one bad import breaks startup
- Python syntax errors stop Django before migrations run
- Django field arguments are strict (`choices` vs `choice`, field names, etc.)
- Keep app boundaries clean (`parts` admin ≠ `stock` admin)

---

## 🚧 Remaining Work (Roadmap)

### 1️⃣ Seed & Demo Data
- [ ] Create warehouse location(s)
- [ ] Create multiple technician locations
- [ ] Populate 20–50 realistic parts
- [ ] Add RECEIVE / ISSUE ledger entries for demo realism

### 2️⃣ On-Hand Inventory Calculation
- [ ] Derive current stock by summing ledger entries per `(location, part)`
- [ ] Create read-only inventory view (warehouse & technician)

### 3️⃣ Low-Stock Alerts
- [ ] Add reorder threshold model or field
- [ ] Identify parts below threshold per location
- [ ] Display alerts in UI

### 4️⃣ Parts Request Workflow (Core Business Feature)
- [ ] Create `Request` model (status-driven)
- [ ] Create request line items
- [ ] Supervisor approval flow
- [ ] Fulfillment generates ISSUE ledger entries

### 5️⃣ Role-Based Access Control (RBAC)
- [ ] Define roles: Technician / Supervisor / Parts Manager / Admin
- [ ] Restrict views and actions by role
- [ ] Ensure techs only see their inventory

### 6️⃣ Audit Hardening
- [ ] Require reason for ADJUST actions
- [ ] Prevent editing/deleting ledger rows
- [ ] Use corrective entries instead of edits

### 7️⃣ User-Facing UI (Beyond Admin)
- [ ] Dashboard (counts, alerts)
- [ ] Parts search page
- [ ] Inventory by location
- [ ] Request submission & approval pages

### 8️⃣ API Layer (Future-Proofing)
- [ ] Add Django REST Framework
- [ ] Expose APIs for parts, inventory, requests, ledger

### 9️⃣ Deployment & Hosting

**External PoC**
- [ ] Dockerize app
- [ ] Move from SQLite → Postgres
- [ ] Host on external VPS or lab environment
- [ ] HTTPS + basic access controls

**Internal Non-Prod (Post-Approval)**
- [ ] Deploy to internal VM
- [ ] Integrate enterprise SSO
- [ ] Central logging & backups

---

## 🏁 Current State Summary

> TROI now has a **working inventory core**:
> - Parts catalog
> - Locations
> - Auditable inventory ledger
> - Admin UI for all core objects

This is a **credible, demo-ready Proof of Concept** suitable for GitHub and internal pilot discussions.

---

## 🔖 Suggested Git Tags
- `troi-mvp-01` — Parts + Stock Ledger Foundation
- `troi-mvp-02` — On-Hand Inventory + Requests (planned)

---

*Last updated:* _(Jan 31, 2026 0700EST)_
