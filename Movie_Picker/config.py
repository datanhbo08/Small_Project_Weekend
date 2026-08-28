import os
from dotenv import load_dotenv

load_dotenv()  # reads .env into environment variables

TMDB_API_KEY = os.getenv("TMDB_API_KEY")

if not TMDB_API_KEY:
    raise RuntimeError(
        "TMDB_API_KEY not found. Copy .env.example to .env and add your key."
    )