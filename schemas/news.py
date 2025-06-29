# schemas/news.py
from pydantic import BaseModel
from typing import Optional

class NewsArticle(BaseModel):
    title: str
    url: str
    description: Optional[str] = None
    published_at: Optional[str] = None
    source: Optional[str] = None
    author: Optional[str] = None
    content: Optional[str] = None
    language: Optional[str] = "en"
