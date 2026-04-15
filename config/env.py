import os
from config.settings import settings

def setup_env():
    os.environ["OPENAI_API_KEY"] = settings.OPENAI_API_KEY
    os.environ["OPENAI_MODEL_NAME"] = "gpt-4o-mini"