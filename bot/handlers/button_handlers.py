from telegram import Update
from telegram.ext import ContextTypes
from bot.utils.api_client import APIClient
from database.mongo_client import get_user, update_user
from bot.handlers.btc_address import handle_new_btc_address

async def buy_sol(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.callback_query.from_user
    existing_user = await get_user(user.id)
    if not existing_user:
        await update.callback_query.message.reply_text("You are not registered. Please register first using /start.")
        return

    await update.callback_query.message.reply_text(
        f"Please send BTC to the following address to buy and receive SOL at the address we created for you. "
        f"Please export the private key and keep it safe:\n\n{existing_user['btc_address']}"
    )

async def export_key(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.callback_query.from_user
    existing_user = await get_user(user.id)
    if not existing_user:
        await update.callback_query.message.reply_text("You are not registered. Please register first using /start.")
        return

    api_response = await APIClient.export_key(user.id, existing_user['api_key'])
    print(api_response)
    if api_response:
        await update.callback_query.message.reply_text(f"Your Solana Private Key: {api_response['private_key']}")
    else:
        await update.callback_query.message.reply_text("Failed to export key. Please try again later.")

# Add other button handlers here (update_btc_address, tx_settings, autobuy_settings)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    if query.data == 'buy_sol':
        await buy_sol(query, context)
    elif query.data == 'export_key':
        await export_key(query, context)
    elif query.data == 'handle_new_btc_address':
        await handle_new_btc_address(query, context)
    elif query.data == 'tx_settings':
        await query.edit_message_text(
            text="TX Settings functionality is under development.")
    elif query.data == 'autobuy_settings':
        await query.edit_message_text(
            text="Autobuy Settings functionality is under development.")