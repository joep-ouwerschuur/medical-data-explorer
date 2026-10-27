# Medical Data Explorer — Project Intent

## Purpose

Medical Data Explorer is a personal learning and portfolio project focused on building reliable software for exploring and processing medical data.

The project already has an initial implementation. **Build on the existing codebase rather than starting over.** First inspect the current architecture, dependencies, functionality, and conventions before proposing changes.

The goal is not merely to create a visually appealing dashboard. The primary goal is to develop practical software engineering and data engineering skills in a healthcare-related context.

## Background and career interests

I am studying for an Associate Degree in Software Development. My preferred long-term direction is **Data Engineering, ideally Healthcare Data Engineering**, with **Backend Software Engineering** as a strong alternative.

My interests include:

- Medical and healthcare technology, and potentially bioinformatics.
- Python, SQL, PostgreSQL, Java, and TypeScript.
- Data pipelines, data integration, and data modeling.
- Reliable backend systems and APIs.
- Data quality, testing, privacy, and security.
- Medical interoperability standards such as HL7 FHIR.
- Docker, cloud infrastructure, and deployment, when justified by the project's maturity.

I want this project to support my learning, portfolio, and preparation for a software development internship, preferably in a medical, data, or backend environment.

## Technical learning priorities

Prioritize these capabilities, roughly in this order, while accounting for what is already implemented:

1. **Data modeling and SQL:** Design understandable relational schemas, relationships, constraints, and useful queries, preferably using PostgreSQL where appropriate.
2. **Python data processing:** Import, validate, clean, transform, and load datasets through a reproducible ETL/ELT workflow.
3. **Data quality and reliability:** Handle missing or invalid values, duplicates, unexpected input, and repeat runs safely. Add logging and meaningful automated tests.
4. **Backend engineering:** Expose data through well-designed APIs, with clear HTTP behavior, validation, error handling, filtering, and pagination when relevant.
5. **Reproducible development:** Use Git, clear documentation, environment configuration, and Docker where useful.
6. **Healthcare domain knowledge:** Learn the structure and limitations of medical datasets; explore HL7 FHIR when it serves a concrete use case.
7. **Frontend and visualization:** Provide a usable interface to explore the data, without letting UI polish overshadow the data and backend foundations.
8. **Advanced tooling:** Consider cloud deployment, orchestration, dbt, or Airflow only after there is a concrete need.

These are **learning priorities, not instructions to replace the existing tech stack**. Evaluate alternatives based on educational value, simplicity, and compatibility with the current project.

## Intended outcome

Aim for a small but complete, demonstrable system that can:

- Ingest an appropriately licensed public or synthetic medical dataset.
- Validate and transform data with explainable rules.
- Store structured data and query it effectively.
- Make relevant results accessible through an API and, if useful, a simple interface.
- Demonstrate tests, sensible error handling, and reproducible setup.
- Explain architectural decisions and trade-offs in documentation.

The project does not need every feature at once. Prefer a working end-to-end vertical slice over many partially implemented features.

## How Codex should help

**Learning is more important than generating code quickly.**

- Inspect the existing implementation before making recommendations or changes.
- Preserve working functionality and existing architectural decisions unless there is a clear reason to change them.
- Explain the reasoning behind important technical choices and trade-offs.
- Prefer small, incremental changes that I can understand, implement, test, and review.
- Help me think through problems; do not automatically deliver large complete solutions when guided implementation would teach me more.
- When I ask for code, keep it focused and explain non-obvious parts.
- Encourage clean code, appropriate abstractions, security, tests, and maintainability without overengineering.
- Suggest what I should learn next based on the current codebase and the highest-value skill gaps.
- Distinguish requirements from optional improvements. Ask before introducing major dependencies, frameworks, or architectural rewrites.
- Help me document and explain my own design and implementation decisions for my portfolio.

## Scope and boundaries

- Use **synthetic, anonymized where genuinely appropriate, or public datasets with suitable usage rights**. Do not introduce real identifiable patient data.
- Treat health data as sensitive. Avoid logging personal or sensitive information; consider privacy and security in design decisions.
- Do not present exploratory analyses as clinical advice or validated medical conclusions.
- Do not add machine learning, microservices, Kubernetes, or complex cloud infrastructure simply for portfolio appeal.
- Keep the workload manageable alongside my studies and other projects. Sustainable progress and depth of understanding matter more than feature count.

## Decision principle

When choosing the next task, favor the smallest meaningful improvement that strengthens **data engineering fundamentals, backend reliability, or healthcare domain understanding**, while keeping the existing application functional.

This document describes my intentions and learning goals. It is **not** a claim that these features or technologies are already implemented. The actual repository is the source of truth for the project's current state.
