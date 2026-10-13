# Week 3: Architecture, Database Model, API Plan, and Technology Prototype

Proposal milestone: *"Architecture, database model, API plan, technology prototype"* (9 hours).

| Time | Task | Deliverable | Status |
|---|---|---|---|
| 2 h | Architecture | [01_architecture.md](01_architecture.md) | Draft complete |
| 2 h | Database model | [02_database_model.md](02_database_model.md) + [schema_draft.sql](../../database/schema_draft.sql) | Draft complete |
| 2 h | API plan | [03_api_plan.md](03_api_plan.md) | Draft complete |
| 3 h | Technology prototype | [04_prototype.md](04_prototype.md) + [backend/](../../backend/) | Working, 4 tests passing |

## Completion checklist

- [ ] I can explain the difference between the frontend and backend.
- [x] I have a diagram showing how the browser, FastAPI, database, AI service, document processing, and future speech-to-text fit together.
- [x] I have a preliminary database model.
- [ ] I understand what a table, row, column, ID, and relationship mean.
- [x] I have a preliminary list of API endpoints.
- [ ] I understand the basic difference between GET and POST.
- [ ] I can run a FastAPI application locally.
- [ ] I can open or call a FastAPI endpoint and receive JSON.
- [ ] I can send a small structured request to FastAPI and receive a structured response.
- [ ] I saved screenshots or notes showing the prototype working (in [evidence/](evidence/)).

The unchecked items are yours to do: run the prototype on your own machine using
[04_prototype.md](04_prototype.md) and save the screenshots.

## Not in scope this week

Finished UI, the real document upload system, AI comprehension logic, speech-to-text,
the real database, progress tracking, authentication, deployment, and styling. These
belong to Weeks 4–14.

## Hand-off to Week 4

Week 4 turns this plan into the project skeleton: split `main.py` into routers
(`documents`, `sessions`, `responses`) following the API plan, and add stub endpoints
that return placeholder data.
