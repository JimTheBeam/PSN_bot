from db.user.db_user import insert_user_data


def start_command(update, context):
    """Send a message when the command /start is issued."""
    chat_id = update.message.chat.id
    insert_user_data(chat_id)
    text = 'send me name of the game'
    update.message.reply_text(text)



def help_command(update, context):
    """Send a message when the command /help is issued."""
    text = 'Hello from psn bot! \npress /start for start'
    update.message.reply_text(text)


def error_message(update, context):
    """error message when user sent unapropriate data(sticker/foto/etc)."""
    text = 'I don\'t understand you try again \n press /help'
    update.message.reply_text(text)
