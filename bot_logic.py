from db.work_with_db import find_game as find_game_in_db
from utils import create_game_text
from keyboards.game_keyboard import game_keyboard



def return_game(update, context):
    """find a game in db by game's name"""
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
        keyboard = game_keyboard(psn_link=psprices_url, subscription=True)
    context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=game_photo_link,
                        caption=game_text,
                        parse_mode='MarkdownV2',
                        reply_markup=keyboard)