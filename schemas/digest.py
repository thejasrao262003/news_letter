from pydantic import BaseModel
from typing import List, Optional
from schemas.summary import NewsSummary

class NewsDigest(BaseModel):
    date: str
    topic: str = "AI"
    summaries: List[NewsSummary]
    sent_flag: bool = False
    created_at: Optional[str] = None
