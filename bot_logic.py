from db.db_game import find_game as find_game_in_db
from db.user.db_user import is_user_subscribed_game

from keyboards.game_keyboard import game_keyboard
from utils import create_game_text


def return_game(update, context):
    '''find a game in db by game's name'''
    game_name_from_user = update.message.text
    game = find_game_in_db(game_name_from_user)
    if game is None:
        return update.message.reply_text(f'Not found game: {game_name_from_user}')

    game_text = create_game_text(game)
    game_photo_link = game[4]
    if game_photo_link is None:
        return context.bot.send_message(chat_id=update.effective_chat.id,
                                        text=game_text, parse_mode='MarkdownV2')
    psprices_url = game[6]
    if psprices_url is None:
        keyboard = None
    else:
        subscription = is_user_subscribed_game(
                        chat_id=update.effective_chat.id,
                        game_name=game[0])
        if subscription is None:
            subscription = False
        else:
            subscription = True

        keyboard = game_keyboard(psn_link=psprices_url, subscription=subscription)


    context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=game_photo_link,
                        caption=game_text,
                        parse_mode='MarkdownV2',
                        reply_markup=keyboard)