-- ReadSmart preliminary database model (Week 3 DRAFT)
-- Planning artifact only. Real implementation is scheduled for Week 10,
-- and this design is expected to change before then.
--
-- Try it:  sqlite3 readsmart_draft.db < database/schema_draft.sql

PRAGMA foreign_keys = ON;

-- Reading material supplied by the user (pasted text, PDF, or Word file).
CREATE TABLE documents (
    id                INTEGER PRIMARY KEY,
    title             TEXT NOT NULL,
    source_type       TEXT NOT NULL CHECK (source_type IN ('text', 'pdf', 'docx')),
    original_filename TEXT,                -- NULL for pasted text
    extracted_text    TEXT NOT NULL,
    created_at        TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Smaller pieces of a document that the student reads one at a time.
CREATE TABLE sections (
    id             INTEGER PRIMARY KEY,
    document_id    INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    section_number INTEGER NOT NULL,       -- 1, 2, 3 ... order within the document
    section_text   TEXT NOT NULL,
    UNIQUE (document_id, section_number)
);

-- One student's attempt to work through a document.
CREATE TABLE reading_sessions (
    id                     INTEGER PRIMARY KEY,
    document_id            INTEGER NOT NULL REFERENCES documents(id) ON DELETE CASCADE,
    current_section_number INTEGER NOT NULL DEFAULT 1,
    status                 TEXT NOT NULL DEFAULT 'in_progress'
                           CHECK (status IN ('in_progress', 'completed')),
    started_at             TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP,
    completed_at           TEXT
);

-- What the student typed or said after reading a section.
CREATE TABLE responses (
    id            INTEGER PRIMARY KEY,
    session_id    INTEGER NOT NULL REFERENCES reading_sessions(id) ON DELETE CASCADE,
    section_id    INTEGER NOT NULL REFERENCES sections(id) ON DELETE CASCADE,
    response_text TEXT NOT NULL,           -- typed text, or the speech-to-text transcript
    input_type    TEXT NOT NULL CHECK (input_type IN ('typed', 'spoken')),
    submitted_at  TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- The AI evaluation returned for one response.
-- No score / pass-fail column on purpose: the proposal says feedback only.
CREATE TABLE feedback (
    id             INTEGER PRIMARY KEY,
    response_id    INTEGER NOT NULL UNIQUE REFERENCES responses(id) ON DELETE CASCADE,
    praise         TEXT NOT NULL,
    corrections    TEXT,                   -- NULL if nothing was misunderstood
    missed_details TEXT,                   -- NULL if nothing important was missed
    next_step      TEXT NOT NULL,
    created_at     TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
