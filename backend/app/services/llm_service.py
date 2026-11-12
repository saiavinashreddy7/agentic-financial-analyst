from langchain_ollama import ChatOllama

from backend.app.config import settings


class LLMService:
	def __init__(self):
		self.llm = ChatOllama(
			model=settings.OLLAMA_MODEL,
			base_url=settings.OLLAMA_BASE_URL,
			temperature=settings.OLLAMA_TEMPERATURE,
		)

	def generate_response(self, message: str) -> str:
		response = self.llm.invoke(message)
		return response.content


llm_service = LLMService()
