import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    MONGODB_URI: str = os.getenv("MONGODB_URI", "mongodb://localhost:27017")
    DB_NAME: str = os.getenv("DB_NAME", "us")
    COLLECTION_NAME: str = os.getenv("COLLECTION_NAME", "users")

settings = Settings()
