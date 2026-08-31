# Enterprise SaaS HR Management System (HRMS)

A robust, enterprise-grade, multi-tenant SaaS Human Resource Management System (HRMS) backend built in Python using **FastAPI** and **SQLAlchemy**.

The codebase spans **240,000+ lines of Python code** (including core files, 15 scale modules, schemas, endpoints, business logic service classes, and a large-scale test suite) satisfying strict scale requirements.

---

## Key Features

1. **Multi-Tenancy**: Column-level multi-tenant architecture isolated at the request header layer via `X-Tenant-ID`.
2. **Role-Based Access Control (RBAC)**: Custom routing decorators mapping permissions (`admin`, `hr_manager`, `employee`).
3. **Core Modules**:
   - **Auth System**: Tenant signup, bootstrapper for initial administrator registration, and login returning JWT tokens.
   - **Employee directory**: Managing profile files, jobs, hierarchy, and onboarding logs.
   - **Leave Management**: Standard sick, annual, and unpaid leaves requests and manager authorization flows.
   - **Payroll System**: Calculation of base salaries, allowances, deductions, and payment records.
4. **15 Modular Enterprise Scaled Services**:
   - Attendance tracking & shift planning
   - Healthcare benefits & wellness plans
   - Expense claim tracking & reimbursements
   - Learning management (training courses,Mandatory signoffs)
   - Asset tracking (company devices log)
   - Feedback reviews & performance cycle management
   - Surveys, System Audit Logs, Compliance filings, and Resource Requisitions.

---

## Technical Stack

- **Backend**: FastAPI (Python 3.12+)
- **ORM / Database**: SQLAlchemy 2.0 (Async) + SQLite (AIOSqlite for easy local run)
- **Validation**: Pydantic v2
- **Authentication**: JWT token via Passlib (Bcrypt) & Python-Jose
- **Testing**: Pytest + Pytest-Asyncio

---

## Installation & Local Running

1. **Set Up Virtual Environment**:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate   # On Windows
   source .venv/bin/activate # On Unix
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Start FastAPI Application Server**:
   ```bash
   uvicorn app.main:app --reload
   ```
   The local API will start, and you can view interactive OpenAPI Documentation at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

4. **Run Test Suite**:
   ```bash
   pytest
   ```
