from dotenv import load_dotenv
import os

load_dotenv()

class Settings:
    OLLAMA_MODEL = os.getenv("OLLAMA_MODEL")
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    DB_URL = os.getenv("DB_URL")
    
    
settings = Settings()