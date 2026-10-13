"""ReadSmart Week 3 technology prototype.

This small FastAPI app answers one question: can a Python FastAPI server
receive a request from a client and send back structured JSON?

Run it from the backend/ folder:
    uvicorn app.main:app --reload

Then open http://127.0.0.1:8000/health or the interactive docs at
http://127.0.0.1:8000/docs
"""

from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(
    title="ReadSmart API (Week 3 Prototype)",
    description="Technology prototype for the ReadSmart reading comprehension tutor.",
    version="0.1.0",
)


# --- Request / response shapes -------------------------------------------
# Pydantic models describe the JSON we expect. FastAPI uses them to parse
# and validate incoming data, and to document the endpoint at /docs.


class HealthResponse(BaseModel):
    status: str


class StudentResponseIn(BaseModel):
    section: str = Field(
        min_length=1,
        description="The source reading section the student just read.",
        examples=["The dog ran through the park."],
    )
    student_response: str = Field(
        min_length=1,
        description="The student's typed explanation of the section.",
        examples=["The dog went to the park."],
    )


class StudentResponseOut(BaseModel):
    section_received: bool
    response_received: bool
    section_word_count: int
    response_word_count: int


# --- Prototype 1: health endpoint -----------------------------------------


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    """Prove the server is running and reachable."""
    return HealthResponse(status="ReadSmart API is running")


# --- Prototype 2: accept a student response -------------------------------


@app.post("/prototype/response", response_model=StudentResponseOut)
def receive_student_response(payload: StudentResponseIn) -> StudentResponseOut:
    """Prove structured data can travel from a client to the backend.

    No AI yet; this only confirms both fields arrived and were parsed.
    In Week 7 this becomes the real POST /responses + POST /evaluate flow.
    """
    return StudentResponseOut(
        section_received=True,
        response_received=True,
        section_word_count=len(payload.section.split()),
        response_word_count=len(payload.student_response.split()),
    )
