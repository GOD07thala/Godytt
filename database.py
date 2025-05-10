from pymongo import MongoClient
from config import MONGO_URL

client = MongoClient(MONGO_URL)
db = client.botmaker

def save_user_bot(user_id, token):
    db.userbots.insert_one({"user_id": user_id, "token": token})

def get_user_bots(user_id):
    return list(db.userbots.find({"user_id": user_id}))
