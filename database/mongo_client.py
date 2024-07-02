from motor.motor_asyncio import AsyncIOMotorClient
from bot.config import MONGO_URI

client = AsyncIOMotorClient(MONGO_URI)
db = client['telegram_bot']
users_collection = db['users']

async def get_user(user_id: int):
    return await users_collection.find_one({"user_id": user_id})

async def create_user(user_data: dict):
    return await users_collection.insert_one(user_data)

async def update_user(user_id: int, update_data: dict):
    return await users_collection.update_one({"user_id": user_id}, {"$set": update_data})

# Add other database operations here