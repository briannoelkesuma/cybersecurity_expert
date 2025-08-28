# backend/app/api_router.py
from fastapi import APIRouter, HTTPException
from . import schemas
from .services import rag_service, trends_service, feedback_service

router = APIRouter()

# --- Chatbot Endpoint ---
@router.post("/chat/query", response_model=schemas.QueryResponse, tags=["Chatbot"])
async def handle_chat_query(request: schemas.QueryRequest):
    try:
        answer, sources = rag_service.answer_question(request.query)
        return schemas.QueryResponse(answer=answer, sources=sources)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing query: {e}")

# --- Feedback Endpoint ---
@router.post("/chat/feedback", response_model=schemas.FeedbackResponse, tags=["Chatbot"])
async def handle_user_feedback(request: schemas.FeedbackRequest):
    feedback_service.log_feedback(request)
    return schemas.FeedbackResponse(status="success", message="Feedback received, thank you!")

# --- Dashboard Endpoints ---
@router.get("/dashboard/trends", response_model=schemas.HotTopicsResponse, tags=["Dashboard"])
async def get_hot_topics():
    topics = trends_service.get_hot_topics()
    return schemas.HotTopicsResponse(topics=topics)

@router.get("/dashboard/gaps", response_model=schemas.KnowledgeGapResponse, tags=["Dashboard"])
async def get_knowledge_gaps():
    gaps = trends_service.identify_knowledge_gaps()
    return schemas.KnowledgeGapResponse(gaps=gaps)