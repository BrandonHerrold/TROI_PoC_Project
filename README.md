# TROI
# Technician Resources and Operational Index (PoC)

A Django-based **proof of concept** for managing technician parts inventory using an **audit-first, ledger-driven design**.

This project demonstrates how to model, track, and audit inventory movements (receive, issue, transfer, adjust) across warehouses and technician locations in a way that is **safe, traceable, and enterprise-ready**.

> ⚠️ **Disclaimer**
> This repository is a **generic, non-production PoC**. It contains no proprietary data, credentials, internal URLs, or company-specific integrations. Names, workflows, and data models are intentionally generalized.

---

## 🚀 Why This Project Exists

Most inventory systems store *current counts* and treat history as an afterthought. That approach makes audits, investigations, and error recovery difficult.

This PoC flips that model:

* Inventory is derived from an **append-only ledger**
* Every movement is attributable to a user, time, and reason
* Corrections are recorded as new events, not silent edits

This pattern mirrors real-world best practices used in:

* enterprise asset tracking
* financial systems
* security-sensitive environments

---

## ✨ Key Features

* **Parts Catalog**

  * Unique part numbers
  * Units of measure
  * Active/inactive lifecycle

* **Locations**

  * Warehouse
  * Technician
  * Extensible for future location types

* **Inventory Ledger (Core Concept)**

  * RECEIVE / ISSUE / TRANSFER / ADJUST actions
  * Immutable, append-only history
  * Inline line items per transaction

* **Audit-Friendly by Design**

  * Who did what
  * When it happened
  * Where inventory moved
  * Why it changed (reference + notes)

* **Admin-Driven PoC UI**

  * Rapid prototyping via Django Admin
  * Clean separation of apps and responsibilities

---

## 🧱 Architecture Overview

```
Django Project
│
├── parts/        # Parts catalog (what exists)
├── stock/        # Locations + inventory ledger (what happened)
├── troi/         # Project configuration
└── docs/         # Architecture notes and roadmap
```

### Design Principles

* **Ledger-first** (history is source of truth)
* **Explicit state changes** (no hidden mutations)
* **Separation of concerns** (catalog vs movement)
* **Enterprise-safe PoC** (upgrade path in mind)

---

## 🛠 Tech Stack

* **Python 3.12**
* **Django**
* **SQLite** (local PoC only)
* **Django Admin** (rapid UI + validation)

Planned upgrades:

* PostgreSQL
* Django REST Framework
* Dockerized deployment

---

## ▶️ Getting Started (Local)

```bash
# create virtual environment
python -m venv .venv

# activate (Windows)
.venv\Scripts\Activate.ps1

# install dependencies
pip install django

# run migrations
cd app
python manage.py migrate

# create admin user
python manage.py createsuperuser

# start server
python manage.py runserver
```

Visit:

* [http://127.0.0.1:8000/admin](http://127.0.0.1:8000/admin)

---

## 📊 What This PoC Demonstrates

* Real-world Django project structure
* Correct use of migrations and admin configuration
* Inventory modeled as **events**, not counters
* Clean Git hygiene and documentation
* Safe external publication of an internal-style system

This project is intentionally scoped to show **systems thinking**, not just CRUD screens.

---

## 🧭 Roadmap

Planned next steps:

* On-hand inventory views (derived from ledger)
* Low-stock alerts
* Technician request & approval workflow
* Role-based access control (RBAC)
* REST API layer
* Dockerized PoC deployment

See the full checklist here:

* [`docs/troi_progress_checklist_roadmap.md`](docs/troi_progress_checklist_roadmap.md)

## 📄 License

MIT License — see `LICENSE` for details.

---

## 🙋‍♂️ About

This project was built as a **learning-forward, portfolio-quality PoC** focused on:

* backend system design
* auditability
* maintainability
* enterprise readiness

## License

This project is proprietary and confidential.

All rights are reserved by the author.  
No part of this repository may be copied, reproduced, modified,
or redistributed without explicit written permission.

Feedback and discussion are welcome.
