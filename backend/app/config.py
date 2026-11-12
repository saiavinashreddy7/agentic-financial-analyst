from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
	APP_NAME: str = "Agentic Financial Analyst"
	APP_VERSION: str = "0.1.0"
	DEBUG: bool = True

	OLLAMA_BASE_URL: str = "http://localhost:11434"
	OLLAMA_MODEL: str = "llama3.2:latest"
	OLLAMA_TEMPERATURE: float = 0.2

	model_config = SettingsConfigDict(
		env_file=".env",
		env_file_encoding="utf-8",
		extra="ignore",
	)


settings = Settings()
