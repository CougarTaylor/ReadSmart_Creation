# Week 3 – Task C: API Plan

These are the operations the frontend will eventually need from the FastAPI backend.
It is a starting design, not a contract; endpoints can be renamed, combined, or split
as the project is built. ✅ = implemented in the Week 3 prototype.

## Endpoint table

| Method / Endpoint | Purpose | Input | Output | Week |
|---|---|---|---|---|
| ✅ `GET /health` | Check the backend is running. | Nothing | `{"status": "ReadSmart API is running"}` | 3 |
| ✅ `POST /prototype/response` | Prototype only: prove structured data reaches the backend. Replaced later by `/responses`. | `section`, `student_response` | `section_received`, `response_received`, word counts | 3 |
| `POST /documents` | Send pasted text or upload a PDF/Word file. Backend extracts text and creates sections. | JSON `{title, text}` **or** multipart file upload | `{document_id, title, section_count}` | 5 |
| `GET /documents/{id}` | Get basic info about a document. | Document ID | `{id, title, source_type, section_count}` | 5 |
| `GET /documents/{id}/sections` | List the reading sections of a document. | Document ID | `[{section_id, section_number, section_text}, ...]` | 6 |
| `POST /sessions` | Start a reading session for a document. | `{document_id}` | `{session_id, current_section_number}` | 6 |
| `GET /sessions/{id}/current-section` | Get the section the student should read now. | Session ID | `{section_id, section_number, section_text, total_sections}` | 6 |
| `POST /responses` | Submit a typed response; evaluates it and returns feedback. | `{session_id, section_id, response_text, input_type}` | `{response_id, feedback, next_action}` | 7 |
| `POST /evaluate` | Evaluate a response against its source section (no saving). Useful for testing prompts. | `{section_text, response_text}` | `{praise, corrections, missed_details, next_step}` | 7 |
| `POST /sessions/{id}/advance` | Move to the next section after reading feedback. | Session ID | `{current_section_number, status}` | 8 |
| `POST /speech/transcribe` | Convert recorded audio to text. | Audio file (multipart) | `{transcript}` | 9 |
| `GET /sessions/{id}/progress` | Get basic progress. | Session ID | `{current_section_number, total_sections, status, responses_submitted}` | 10 |

## Example request and response bodies

`POST /responses`

```json
{
  "session_id": 12,
  "section_id": 40,
  "response_text": "The dog went to the park.",
  "input_type": "typed"
}
```

Response:

```json
{
  "response_id": 87,
  "feedback": {
    "praise": "Nice job noticing that the dog went to the park!",
    "corrections": null,
    "missed_details": "The section says the dog *ran* through the park.",
    "next_step": "When you're ready, continue to the next section."
  },
  "next_action": "advance"
}
```

The `feedback` object matches the `feedback` table in the database model. Note there is no
score field.

## Error responses (planned)

| Status | When |
|---|---|
| `400 Bad Request` | Unsupported file type, or extraction produced no usable text (e.g., scanned PDF). |
| `404 Not Found` | Document, section, or session ID does not exist. |
| `422 Unprocessable Entity` | Request body has the wrong shape (FastAPI does this automatically). |
| `502 Bad Gateway` | OpenAI or speech-to-text service failed; the frontend should show a friendly retry message. |

## GET vs. POST

- **GET** = "give me information." It doesn't change anything (`GET /health`).
- **POST** = "here is information to process or create" (`POST /responses`).

## What `{id}` means

Braces mark a variable part of the URL. `GET /sessions/12/current-section` asks for the
current section of session 12, so one endpoint works for every session.
