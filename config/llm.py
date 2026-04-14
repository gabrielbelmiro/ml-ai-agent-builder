from crewai import LLM
from config.settings import settings

def get_llm():
    return LLM(
        model="openai/gpt-4o-mini",  
        api_key=settings.OPENAI_API_KEY
    )