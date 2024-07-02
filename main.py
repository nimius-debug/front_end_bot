import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler
from bot.config import TELEGRAM_BOT_TOKEN
from bot.handlers.start import start
from bot.handlers.btc_address import handle_btc_address, update_btc_address, handle_new_btc_address
from bot.handlers.menu import show_menu
from bot.handlers.button_handlers import button

def main() -> None:
    """Start the bot."""
    application = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    # Checks if new user or is registered, creates user in db with empty fields
    application.add_handler(CommandHandler("start", start))

    # Generates new deposit address
    application.add_handler(CommandHandler("updatebtc", update_btc_address))
    application.add_handler(CommandHandler("menu", show_menu))
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_btc_address))
    application.add_handler(
        MessageHandler(filters.TEXT & filters.REPLY, handle_new_btc_address))
    application.add_handler(CallbackQueryHandler(button))

    # Start the Bot
    application.run_polling()

if __name__ == '__main__':
    main()