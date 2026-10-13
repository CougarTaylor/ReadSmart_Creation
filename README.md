# ReadSmart: An AI-Powered Reading Comprehension Tutor

CSE 499 Senior Project, Cougar Taylor.

ReadSmart helps students in grades 4–8 practice active reading. A student reads a short
section of text, explains it in their own words (typed or spoken), and gets encouraging AI
feedback about what they understood, what they missed, and what to do next.

## Repository layout

```
backend/          FastAPI backend (Python)
  app/main.py     Week 3 technology prototype
  tests/          pytest tests
database/         Database schema drafts
docs/week3/       Week 3 architecture, database model, API plan, prototype guide
```

## Quick start

```bash
cd backend
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload     # then open http://127.0.0.1:8000/docs
pytest                            # run tests
```

## Progress

- [x] Week 3: Architecture, database model, API plan, technology prototype ([docs/week3](docs/week3/README.md))
