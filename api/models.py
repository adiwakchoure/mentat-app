from pydantic import BaseModel, HttpUrl
from typing import List

class Query(BaseModel):
    query: str

class UrlRelevance(BaseModel):
    url: str
    is_relevant: bool
    score: float
    insights: List[str]