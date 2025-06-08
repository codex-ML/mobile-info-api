from pymongo import MongoClient
from .config import settings

client = MongoClient(settings.MONGODB_URI)
db = client[settings.DB_NAME]
collection = db[settings.COLLECTION_NAME]

def get_user_by_mobile(mobile: str):
    return list(collection.find({"mobile": mobile}, {"_id": 0}))
