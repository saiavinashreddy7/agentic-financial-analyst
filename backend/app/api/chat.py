from fastapi import APIRouter, HTTPException

from backend.app.config import settings
from backend.app.schemas.chat import ChatRequest, ChatResponse
from backend.app.services.llm_service import llm_service

router = APIRouter(
	prefix="/api/v1",
	tags=["AI Chat"],
)


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
	try:
		answer = llm_service.generate_response(request.message)
		return ChatResponse(
			question=request.message,
			answer=answer,
			model=settings.OLLAMA_MODEL,
			status="success",
		)
	except Exception as error:
		raise HTTPException(
			status_code=503,
			detail=f"AI service unavailable: {str(error)}",
		)
