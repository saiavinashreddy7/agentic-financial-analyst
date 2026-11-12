from pydantic import BaseModel, Field


class ChatRequest(BaseModel):
	message: str = Field(
		...,
		min_length=1,
		max_length=10000,
		description="User's financial question",
	)


class ChatResponse(BaseModel):
	question: str
	answer: str
	model: str
	status: str
