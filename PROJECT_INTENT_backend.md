# Medical Data Explorer — Project Intent

## Purpose

Medical Data Explorer is my primary personal learning and portfolio project alongside my Associate Degree in Software Development. Its current purpose is to help me become a capable **Python Backend Engineer** and prepare for a backend-focused internship starting around February 2027, preferably in healthcare IT.

The project already has an initial implementation. **Inspect and build on the existing codebase; do not start over by default.** Review the current architecture, dependencies, functionality, tests, and conventions before recommending changes.

The main outcome is not a polished dashboard, sophisticated analytics, or an elaborate data platform. It is a **small, reliable, well-designed backend** that I can build, explain, test, and maintain myself.

## Career and learning direction

My current primary direction is **Backend Software Engineering**, with an interest in **data-intensive systems and healthcare applications**. Data Engineering remains a possible future specialization, but it is not the immediate focus of this project.

My degree already provides experience with Java, TypeScript, HTTP, SQL, teamwork, and full-stack development. In this personal project I want to deepen transferable backend engineering fundamentals through **Python**, ideally **FastAPI** where compatible with the existing codebase.

Prioritize understanding concepts over collecting technologies. Avoid unnecessary language or framework switching.

## Technical priorities

Prioritize these roughly in order, adapting to the current implementation and genuine project needs:

1. **Python fundamentals:** Clear modules, functions, classes where appropriate, type hints, exceptions, dependency management, and readable code.
2. **HTTP and API design:** RESTful endpoints, request/response models, JSON, status codes, validation, filtering, pagination where justified, and consistent error handling. Prefer FastAPI if adopting it is reasonable.
3. **Backend architecture:** Separation of API, application/business logic, and persistence concerns; dependency injection where useful; maintainable boundaries without premature abstraction.
4. **SQL and PostgreSQL:** Relational modeling, keys, constraints, joins, indexes when needed, transactions, parameterized queries, and migrations.
5. **Testing and debugging:** pytest unit and integration tests, meaningful edge cases, debugging, logging, and reproducible bug fixes.
6. **Security and reliability:** Input validation, secrets management, safe database access, authentication/authorization when there is a real use case, safe handling of errors, and privacy-aware design.
7. **Professional workflow:** Git, small commits, code review habits, documentation, environment configuration, Docker and Docker Compose where useful.
8. **Deployment and CI:** Basic CI for linting/testing and a simple deployment only after the core backend works reliably.
9. **Healthcare context:** Use suitable synthetic or licensed public medical datasets; learn medical data structures and consider HL7 FHIR only when it supports a concrete feature.

**Not current priorities:** Airflow, dbt, advanced ETL/ELT orchestration, data warehouses, distributed data platforms, machine learning, Kubernetes, microservices, or elaborate frontend development. Small, necessary import/validation steps are fine, but should support the backend rather than become a separate data engineering project.

These are learning goals, **not claims about what is already implemented** and not permission to replace the existing stack automatically.

## Intended outcome

Work toward one modest end-to-end application that can:

- Load a small, appropriately licensed public or synthetic medical dataset.
- Store and retrieve structured records through PostgreSQL or an existing suitable database.
- Expose clear, documented API endpoints for querying, filtering, and updating records where appropriate.
- Validate input and return predictable HTTP errors.
- Keep domain logic separate from transport and persistence details.
- Demonstrate meaningful automated tests and basic security practices.
- Run reproducibly locally, preferably with Docker when helpful.
- Explain design choices, trade-offs, and limitations in a concise README.

A minimal existing frontend may remain if useful for demonstrating the backend, but **frontend features and visual polish are secondary**. Prefer one working vertical slice to a long feature list.

## How AI coding agents should collaborate

**My learning and independent problem-solving take priority over implementation speed.**

- First inspect the repository and explain what exists before proposing work.
- Default to **guidance, questions, short explanations, and small implementation steps** so I write and understand the code myself.
- **Do not edit, create, delete, or refactor project files unless I explicitly request an implementation and confirm that you may make changes.** A general request for advice or a plan is not permission to modify files.
- When I request help with a problem, start with the smallest useful hint or explanation; provide complete code only when I ask for it.
- Explain important design choices, alternatives, and trade-offs. Be critical of unnecessary complexity.
- Preserve working functionality and established conventions unless a change is justified and approved.
- Propose focused tests and edge cases; distinguish verified behavior from assumptions.
- Favor small, reviewable changes and help me understand any code that is produced.
- Ask before adding significant dependencies, switching frameworks, changing database technology, or redesigning architecture.
- Help me produce portfolio documentation that accurately reflects what I personally built and understood.
- Recommend the next task based on the current codebase, internship readiness, and the highest-value backend skill gap.

## Scope and boundaries

- Use only synthetic data or public datasets with suitable licenses; do not introduce identifiable patient data. Anonymization must be genuinely sufficient, not assumed.
- Treat health-related information as potentially sensitive. Do not log secrets or sensitive records.
- Do not present exploratory data output as clinical advice or validated medical conclusions.
- Do not add infrastructure or abstractions merely to impress recruiters.
- Keep scope realistic alongside my studies. Depth, consistency, and sustainable progress matter more than speed or feature count.
- Avoid turning this into a second full-stack school project; use the personal project primarily to deepen Python backend engineering.

## Decision principle

When selecting the next task, choose the **smallest meaningful backend improvement** that strengthens Python, HTTP/API design, architecture, SQL, testing, security, or deployment while preserving a functional application.

The repository is the source of truth for its actual implementation. This document describes **intent and priorities**, not completed features.
