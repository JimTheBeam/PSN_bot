from db.db_game import find_game as find_game_in_db
from db.user.db_user import is_user_subscribed_game

from keyboards.game_keyboard import game_keyboard
from utils import create_game_text, convert_game_tuple_to_dict


def return_game(update, context):
    '''find a game in db by game's name'''
    game_name_from_user = update.message.text
    game = find_game_in_db(game_name_from_user)
    if game is None:
        return update.message.reply_text(f'Not found game: {game_name_from_user}')
    # convert tuple to dict:
    game = convert_game_tuple_to_dict(game)

    game_text = create_game_text(game)
    game_photo_link = game['image_link']
    if game_photo_link is None:
        return context.bot.send_message(chat_id=update.effective_chat.id,
                                        text=game_text, parse_mode='MarkdownV2')

    if game['psprices_url'] is None:
        keyboard = None
    else:
        subscription = is_user_subscribed_game(
                        chat_id=update.effective_chat.id,
                        game_id=game['game_id'])
        if subscription is None:
            subscription = False
        else:
            subscription = True

        keyboard = game_keyboard(psn_link=game['psprices_url'], subscription=subscription,
                                 game_id=game['game_id'])

    context.bot.send_photo(
                        chat_id=update.effective_chat.id,
                        photo=game_photo_link,
                        caption=game_text,
                        parse_mode='MarkdownV2',
                        reply_markup=keyboard)



def inline_button_pressed(update, context):
    query = update.callback_query
    query.answer()

    query.edit_message_caption(caption=f"Selected option: {query.data}")