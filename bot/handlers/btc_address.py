from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.validators import is_valid_btc_address
from bot.utils.api_client import MockAPIClient as APIClient
from database.mongo_client import get_user, create_user, update_user

async def handle_btc_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.message.from_user
    btc_address = update.message.text

    if not is_valid_btc_address(btc_address):
        await update.message.reply_text("Please provide a valid BTC address.")
        return

    existing_user = await get_user({"btc_address": btc_address})
    if existing_user:
        await update.message.reply_text("This BTC address is already registered.")
        return

    # Using MockAPIClient instead of real API
    api_response = await APIClient.register_user(user.id)
    if api_response:
        user_data = {
            "user_id": user.id,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "btc_address": btc_address,
            "solana_public_key": api_response['solana_public_key'],
            "api_key": api_response['api_key'],
        }
        await create_user(user_data)
        await update.message.reply_text(
            f"Registration successful!\n\n"
            f"Your Solana Public Key: {api_response['solana_public_key']}\n"
            f"Your API Key: {api_response['api_key']}"
        )
    else:
        await update.message.reply_text("Registration failed. Please try again later.")


async def update_btc_address(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the /updatebtc command."""
    user = update.message.from_user if update.message else update.callback_query.from_user
    existing_user =  await get_user({"user_id": user.id})
    if not existing_user:
        await update.message.reply_text(
            "You are not registered. Please register first using /start.")
        return

    await update.message.reply_text("Please provide your new BTC Funding address:")

async def handle_new_btc_address(update: Update,
                                 context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle the new BTC address provided by the user."""
    user = update.message.from_user
    btc_address = update.message.text

    if not is_valid_btc_address(btc_address):
        await update.message.reply_text("Please provide a valid BTC address.")
        return

    # Check if BTC address is already registered
    existing_user = await get_user({"btc_address": btc_address})
    if existing_user:
        await update.message.reply_text(
            "This BTC address is already registered.")
        return

    # Update BTC address in MongoDB
    await update_user({"user_id": user.id},
                                {"$set": {
                                    "btc_address": btc_address
                                }})

    await update.message.reply_text(
        f"Your BTC address has been updated to: {btc_address}")