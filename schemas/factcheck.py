from pydantic import BaseModel
from typing import Optional

class FactCheckResult(BaseModel):
    summary_title: str
    claim: str
    verdict: str
    evidence: Optional[str] = None
    sources: Optional[list[str]] = []
    confidence: Optional[float] = None
