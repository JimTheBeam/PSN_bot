#!/usr/bin/env python
import logging
import os

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

from config import Config
from db.work_with_db import find_game as find_game_in_db


if not os.path.exists('logs'):
    os.mkdir('logs')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
     level=logging.INFO, filename='logs/PSN_bot.log')

logger = logging.getLogger(__name__)
logger.info('bot startup')


def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    text = 'send me name of the game'
    update.message.reply_text(text)


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    text = 'Hello from psn bot! \npress /start for start'
    update.message.reply_text(text)


def return_game(update: Update, context: CallbackContext) -> None:
    """find a game in db by game's name"""
    game_name = update.message.text
    game = find_game_in_db(game_name)
    if game is None:
        return update.message.reply_text('Not found')
    print(game)
    update.message.reply_text('game price: ' + game[0])


def error_message(update: Update, context: CallbackContext) -> None:
    """error message when user sent unapropriate data(sticker/foto/etc)."""
    text = 'I don\'t understand you try again \n press /help'
    update.message.reply_text(text)


def main():
    """Start the bot."""
    updater = Updater(Config.BOT_TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, return_game))

    dp.add_handler(MessageHandler(Filters.all, error_message))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()