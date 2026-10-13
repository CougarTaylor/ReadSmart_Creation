# Week 3 – Task D: FastAPI Technology Prototype

**Question this prototype answers:** Can I run a Python FastAPI server, send it a
request, and receive a structured JSON response?

Code: [`backend/app/main.py`](../../backend/app/main.py)
Tests: [`backend/tests/test_main.py`](../../backend/tests/test_main.py)

## 1. Set up (one time)

From the repository root:

```bash
cd backend
python -m venv .venv
# Windows:      .venv\Scripts\activate
# macOS/Linux:  source .venv/bin/activate
pip install -r requirements.txt
```

## 2. Run the server

```bash
uvicorn app.main:app --reload
```

You should see `Uvicorn running on http://127.0.0.1:8000`. `--reload` restarts the server
whenever you save a code change.

## 3. Prototype 1 – Health endpoint

Open <http://127.0.0.1:8000/health> in a browser. Expected:

```json
{"status": "ReadSmart API is running"}
```

## 4. Prototype 2 – Send a student response

**Easiest way:** open <http://127.0.0.1:8000/docs>. FastAPI generates this page
automatically. Click **POST /prototype/response → Try it out**, paste the body
below, and click **Execute**.

```json
{
  "section": "The dog ran through the park.",
  "student_response": "The dog went to the park."
}
```

Expected response:

```json
{
  "section_received": true,
  "response_received": true,
  "section_word_count": 6,
  "response_word_count": 6
}
```

**From the command line** (macOS/Linux/Git Bash):

```bash
curl -X POST http://127.0.0.1:8000/prototype/response \
  -H "Content-Type: application/json" \
  -d '{"section": "The dog ran through the park.", "student_response": "The dog went to the park."}'
```

**PowerShell:**

```powershell
Invoke-RestMethod -Method Post -Uri http://127.0.0.1:8000/prototype/response `
  -ContentType "application/json" `
  -Body '{"section": "The dog ran through the park.", "student_response": "The dog went to the park."}'
```

Try leaving out `student_response`: FastAPI returns a **422** error explaining which field is
missing. That's validation working without any extra code.

## 5. Run the automated tests

```bash
cd backend
pytest
```

Expected: `4 passed`.

## What this proves

- [x] Python can run the FastAPI application.
- [x] FastAPI can expose a web endpoint.
- [x] A client can send data to the endpoint.
- [x] FastAPI can parse and validate the incoming data.
- [x] Python code can return structured JSON.
- [x] There is a foundation the real ReadSmart frontend can call later.

## Evidence for the weekly report

Save these in `docs/week3/evidence/`:

1. Screenshot of the terminal showing `uvicorn` running.
2. Screenshot of `/health` in the browser.
3. Screenshot of `/docs` showing a successful `POST /prototype/response`.
4. Screenshot of the 422 error when a field is missing.
5. Screenshot of `pytest` output (`4 passed`).

## Optional stretch (only if time remains)

Make a single test call to the OpenAI API from a separate script to confirm your API key
works. Keep the key in a `.env` file (already git-ignored) and never commit it. This
reduces risk for Week 7 but is not required for Week 3.
