Here is the complete issue roadmap with clear Definitions of Done (DoD):

---

### Epic 0: Project Setup & System Foundation

#### Issue #1: Repository Scaffolding, Tooling & AI Guardrails Baseline

* **Scope**: Initialize decoupled directory structure (`backend/`, `frontend/`), Ruff/Black/Prettier configurations, and shared convention documents.
* **Definition of Done**:
* [ ] Directory layout matches the specification (`backend/`, `frontend/`, `docs/`).
* [ ] Linting and formatting configured (Ruff/Black for Python, ESLint/Prettier for frontend) with zero setup warnings.
* [ ] `docs/DECISIONS.md` created to capture architectural choices.


* [ ] AI guardrails committed to the root for agent compliance.





#### Issue #2: Backend App Entrypoint, DB Engine & Healthcheck

* **Scope**: Configure FastAPI lifecycle, SQLAlchemy engine, session factory, CORS middleware, and environment variables.
* **Definition of Done**:
* [ ] `backend/database.py` exports `engine`, `SessionLocal`, and declarative `Base`.
* [ ] `get_db()` dependency yields a database session and guarantees closure on teardown.
* [ ] CORS middleware in `backend/main.py` permits requests from frontend origins.
* [ ] `GET /health` endpoint returns `200 OK` with `{"status": "ok"}`.
* [ ] Smoke test passes for the healthcheck route.



---

### Epic 1: Phase 1 — Asset Manager Module (Full-Stack MVP)

#### Issue #3: Asset Data Models & Pydantic Validation Contracts

* **Scope**: Define ORM entities and data transfer schemas for construction equipment.
* **Definition of Done**:
* [ ] SQLAlchemy model `Asset` defined with fields: `id`, `name`, `serial_number`, `category`, `status` (`Available`, `Checked Out`, `Under Repair`), `assigned_to`, and `last_inspected_at`.
* [ ] Pydantic schemas created: `AssetCreate`, `AssetUpdate`, `AssetCheckoutRequest`, and `AssetResponse`.
* [ ] Enums configured for asset status to prevent invalid string entries.
* [ ] DB tables generate cleanly via SQLAlchemy metadata.



#### Issue #4: Asset CRUD & Checkout State Transition Endpoints

* **Scope**: Build REST endpoints in `backend/routers/assets_router.py` enforcing business logic constraints.
* **Definition of Done**:
* [ ] `GET /api/assets` returns a list of assets with optional query filter for `status`.
* [ ] `POST /api/assets` persists a new asset and returns `201 Created`.
* [ ] `PATCH /api/assets/{id}/checkout` transitions status to `Checked Out` and records `assigned_to`.
* [ ] Attempting to checkout an asset with status `Under Repair` returns an `HTTPException(status_code=400, detail="Cannot check out asset under repair")`.
* [ ] `PATCH /api/assets/{id}/checkin` clears `assigned_to` and resets status to `Available`.
* [ ] Unit and integration tests cover happy paths and 400/404/422 failure scenarios.



#### Issue #5: Frontend Shell & Asset Inventory Dashboard

* **Scope**: Build the primary asset table and status badge interface.
* **Definition of Done**:
* [ ] Clean dashboard view rendering all assets in a responsive table.
* [ ] Status badges visually distinguish `Available` (green), `Checked Out` (blue), and `Under Repair` (red/amber).
* [ ] Search and status filter components update the table without page reloads.
* [ ] Verified at both desktop and mobile viewport widths.





#### Issue #6: Asset Action Modals & API Integration

* **Scope**: Wire frontend forms to the backend API for asset creation, check-out, and check-in.
* **Definition of Done**:
* [ ] Modal form enables creating a new asset with immediate list refresh.
* [ ] Check-out modal prompts for worker assignment and sends `PATCH` payload.
* [ ] Client captures and displays backend 400 error messages (e.g., equipment under repair warnings) clearly.
* [ ] Check-in button resets asset status cleanly with visual UI feedback.



---

### Epic 2: Phase 2 — Daily Site Reporter Module

#### Issue #7: Daily Report DB Models & Schemas

* **Scope**: Design persistence layer for shift logs, safety incidents, and weather snapshots.
* **Definition of Done**:
* [ ] `DailyReport` model created: `id`, `project_name`, `date`, `work_performed`, `headcount`, `delays`, `weather_summary`, and `temperature`.
* [ ] Pydantic schemas defined for report ingestion and response output.
* [ ] Table migrations/creation verified against the database.



#### Issue #8: OpenWeather API Service & Report Router

* **Scope**: Integrate external meteorological service to automatically snapshot weather upon log submission.
* **Definition of Done**:
* [ ] External service client built to fetch live weather based on site location coordinates or city name.
* [ ] API keys loaded securely via environment variables (zero hardcoded secrets).


* [ ] `POST /api/reports` automatically fetches current weather, populates the report, and commits to DB.
* [ ] `GET /api/reports` returns historic site logs in reverse chronological order.
* [ ] Service handles third-party API timeout/failure gracefully by logging a fallback without crashing the report creation.



#### Issue #9: Daily Log Submission & Historic Feed UI

* **Scope**: Frontend views for submitting daily logs and browsing past reports.
* **Definition of Done**:
* [ ] Form for submitting daily operational data (work summary, headcount, notes).
* [ ] Submitted report displays the automatically populated weather badge.
* [ ] Timeline/feed view displaying historic daily entries with date filtering.



---

### Epic 3: Phase 3 — Material & Cost Estimator Module

#### Issue #10: Material Estimation Engine & Calculation Endpoints

* **Scope**: Business logic and REST endpoints for construction procurement formulas.
* **Definition of Done**:
* [ ] Domain logic implemented for concrete volume, drywall surface, and framing lumber calculations.
* [ ] Wastage factor percentage formula correctly applied to output raw vs. recommended order quantities.
* [ ] `POST /api/estimator/calculate` accepts dimensions, material type, and waste buffer, returning cost and quantity breakdowns.
* [ ] Edge cases (e.g., negative dimensions, zero thickness) covered with Pydantic validation tests returning `422`.



#### Issue #11: Interactive Procurement Calculator View

* **Scope**: Frontend interactive calculator view for site supervisors.
* **Definition of Done**:
* [ ] Dynamic form allowing real-time dimension input and material selection.
* [ ] Output card displays required materials, waste buffer addition, and estimated totals.
* [ ] Quick export/copy button to share material lists with procurement teams.



---

### Epic 4: Verification, Security & Final Polish

#### Issue #12: End-to-End System Smoke Tests & Production Build Check

* **Scope**: System validation across all three modules.
* **Definition of Done**:
* [ ] Automated end-to-end integration test runs covering Asset Checkout -> Daily Report -> Material Estimation.
* [ ] Linters and test suites pass with zero warnings across frontend and backend.


* [ ] No temporary `PLACEHOLDER_` flags or dangling `TODO` items left unverified.


* [ ] `README.md` fully documented with local setup, environment variables, and run instructions.



---