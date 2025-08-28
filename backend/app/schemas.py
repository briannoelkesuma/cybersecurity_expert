# backend/app/schemas.py
from pydantic import BaseModel
from typing import List, Optional

# --- Chatbot Schemas ---
class QueryRequest(BaseModel):
    query: str
    user_id: Optional[str] = None

class QueryResponse(BaseModel):
    answer: str
    sources: List[dict] # e.g., [{"title": "...", "url": "..."}]

# --- Feedback Schemas ---
class FeedbackRequest(BaseModel):
    query: str
    response: str
    is_helpful: bool # True for thumbs up, False for thumbs down

class FeedbackResponse(BaseModel):
    status: str
    message: str

# --- Dashboard Schemas ---
class HotTopic(BaseModel):
    topic: str
    summary: str
    article_count: int

class HotTopicsResponse(BaseModel):
    topics: List[HotTopic]

class KnowledgeGap(BaseModel):
    search_term: str
    search_volume: int # Placeholder for Google Trends data
    internal_doc_count: int
    recommendation: str

class KnowledgeGapResponse(BaseModel):
    gaps: List[KnowledgeGap]