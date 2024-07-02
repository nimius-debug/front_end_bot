from telegram import Update
from telegram.ext import ContextTypes
from database.mongo_client import get_user

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    chat_id = update.message.chat_id

    existing_user = await get_user(user.id)
    if existing_user:
        await update.message.reply_text("You are already registered. Use /menu to see more options.")
        return

    await update.message.reply_text("Welcome! Please provide the BTC address you will be funding with to register:")
    context.user_data['chat_id'] = chat_id