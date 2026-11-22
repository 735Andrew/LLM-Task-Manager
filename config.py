from dotenv import load_dotenv
import os

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, ".env"))

LLM_API_TOKEN = os.environ.get("LLM_API_TOKEN")
ACCESS_KEY = os.environ.get("ACCESS_KEY")

STATIC_DIR = basedir + r"\app\static"
KEY_PATTERN = r"^[A-Za-z0-9_-]{8,255}$"
