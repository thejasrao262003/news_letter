from pydantic import BaseModel
from typing import List, Optional
from schemas.news import NewsArticle
from schemas.summary import NewsSummary
from schemas.digest import NewsDigest
from schemas.factcheck import FactCheckResult

class MCPContext(BaseModel):
    stage: str
    articles: Optional[List[NewsArticle]] = None
    summaries: Optional[List[NewsSummary]] = None
    digest: Optional[NewsDigest] = None
    fact_checks: Optional[List[FactCheckResult]] = None
    errors: Optional[List[str]] = []
    meta: Optional[dict] = {}
