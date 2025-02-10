import os

class Config:
    """Global configuration settings."""
    
    USE_DATABASE = os.getenv("USE_DATABASE", "False").lower() == "true"

class OllamaConfig:
    """Centralized configuration for Ollama API integration."""
    
    API_KEY = os.getenv("OLLAMA_API_KEY", "your_default_api_key")
    BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434")
    MODEL_NAME = os.getenv("OLLAMA_MODEL", "llama3")

    @classmethod
    def get_llm_config(cls):
        """Returns the LLM configuration for Ollama."""
        return {
            "model": cls.MODEL_NAME,
            "api_base": cls.BASE_URL,
            "litellm_params": {
                "provider": "ollama",
                "api_key": cls.API_KEY,
                "headers": {"Authorization": f"Bearer {cls.API_KEY}"}
            }
        }
