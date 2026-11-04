from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime, timezone

class Note(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    youtube_url: str
    summary: str
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))