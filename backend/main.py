from fastapi import FastAPI, Depends
from pydantic import BaseModel
from sqlmodel import Session, select
from transcript import get_transcript
from summarizer import summarize_text
from models import Note
from database import init_db, get_session

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

class SummarizeRequest(BaseModel):
    youtube_url: str

@app.get("/")
def root():
    return {"message": "YouTube Summarizer API is running"}

@app.post("/summarize")
def summarize(request: SummarizeRequest, session: Session = Depends(get_session)):
    transcript = get_transcript(request.youtube_url)
    summary = summarize_text(transcript)

    note = Note(youtube_url=request.youtube_url, summary=summary)
    session.add(note)
    session.commit()
    session.refresh(note)

    return note

@app.get("/notes")
def list_notes(session: Session = Depends(get_session)):
    notes = session.exec(select(Note)).all()
    return notes

@app.get("/notes/{note_id}")
def get_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    return note

@app.delete("/notes/{note_id}")
def delete_note(note_id: int, session: Session = Depends(get_session)):
    note = session.get(Note, note_id)
    session.delete(note)
    session.commit()
    return {"message": "Note deleted"}