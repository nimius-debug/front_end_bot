from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ContextTypes
from database.mongo_client import get_user

async def show_menu(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user if update.message else update.callback_query.from_user
    existing_user = await get_user(user.id)
    if not existing_user:
        await update.message.reply_text("You are not registered. Please register first using /start.")
        return

    keyboard = [
        [InlineKeyboardButton("Buy SOL", callback_data='buy_sol')],
        [InlineKeyboardButton("Export Key", callback_data='export_key')],
        [InlineKeyboardButton("TX Settings", callback_data='tx_settings')],
        [InlineKeyboardButton("Update BTC Address", callback_data='update_btc_address')],
        [InlineKeyboardButton("Autobuy Settings", callback_data='autobuy_settings')]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_message = (
        f"Welcome, {existing_user['username']}!\n\n"
        f"Swapping deposits from: {existing_user['btc_address']}\n\n"
        f"Solana Address: {existing_user['solana_public_key']}\n\n"
    )
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)