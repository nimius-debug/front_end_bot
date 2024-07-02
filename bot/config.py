import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
RUST_BACKEND_URL = os.getenv("RUST_BACKEND_URL")
MONGO_URI = os.getenv("MONGO_URI")

# Add any other configuration variables here