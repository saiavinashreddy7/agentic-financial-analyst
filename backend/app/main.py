from fastapi import FastAPI

from backend.app.api.chat import router as chat_router
from backend.app.config import settings

app = FastAPI(
	title=settings.APP_NAME,
	description="AI-powered financial analysis using RAG and Agentic AI",
	version=settings.APP_VERSION,
)

app.include_router(chat_router)


@app.get("/")
def home():
	return {
		"message": "Agentic Financial Analyst API is running!",
		"status": "success",
	}


@app.get("/health")
def health_check():
	return {"status": "healthy"}
