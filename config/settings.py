import os
import keyring
from dotenv import load_dotenv

load_dotenv()

class Settings:
    def __init__(self):
        self.OPENAI_API_KEY = (
            os.getenv("OPENAI_API_KEY") or
            keyring.get_password("openai", "api_key")
        )

        if not self.OPENAI_API_KEY:
            raise ValueError("OPENAI_API_KEY não configurada em nenhuma fonte")

settings = Settings()