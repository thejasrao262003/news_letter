from pydantic import BaseModel

class NewsSummary(BaseModel):
    title: str
    summary: str
    url: str
    source: str
