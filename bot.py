#!/usr/bin/env python3
import logging
import os

from telegram import Update
from telegram.ext import (Updater, CommandHandler, MessageHandler, Filters, 
                          CallbackContext, CallbackQueryHandler)

from config import Config
from bot_logic import return_game, inline_button_pressed

from bot_commands import start_command, help_command, error_message


if not os.path.exists('logs'):
    os.mkdir('logs')

logging.basicConfig(
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
            level=logging.INFO, filename='logs/PSN_bot.log')
logger = logging.getLogger(__name__)
logger.info('bot startup')


def main():
    """Start the bot."""
    updater = Updater(Config.BOT_TOKEN)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, return_game))

    dp.add_handler(CallbackQueryHandler(inline_button_pressed))

    dp.add_handler(MessageHandler(Filters.all, error_message))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()