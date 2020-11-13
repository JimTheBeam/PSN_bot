#!/usr/bin/env python
import logging
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from config import Config


if not os.path.exists('logs'):
    os.mkdir('logs')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
     level=logging.INFO, filename='logs/PSN_bot.log')

logger = logging.getLogger(__name__)
logger.info('bot startup')


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def main():
    """Start the bot."""
    updater = Updater(Config.BOT_TOKEN, use_context=True)

    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()