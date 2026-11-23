from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

LLM_API_TOKEN = os.environ.get("LLM_API_TOKEN")
ACCESS_KEY = os.environ.get("ACCESS_KEY")

STATIC_DIR = os.path.join(basedir, "app", "static")
KEY_PATTERN = r"^[A-Za-z0-9_-]{8,255}$"

LLM_API_URL = "https://foundation-models.api.cloud.ru/v1/chat/completions"

LLM_API_HEADERS = {
    "Authorization": f"Bearer {LLM_API_TOKEN}",
    "Content-Type": "application/json",
}

LLM_API_PAYLOAD = {
    "model": "GigaChat/GigaChat-3-Pro",
    "messages": [
        {
            "role": "system",
            "content": {}, # placeholder for context prompt
        },
        {
            "role": "user",
            "content": {}, # placeholder for manager message
        }
    ],
    "temperature": 0.5
}
