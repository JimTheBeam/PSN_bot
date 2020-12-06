from db.db_game import find_game as find_game_in_db, find_game_price_by_id
from db.user.db_user import is_user_subscribed_game, subscribe_to_game

from keyboards.game_keyboard import game_keyboard
from utils import create_game_text, convert_game_tuple_to_dict, parse_query_data


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
        print(subscription)
        if subscription is None:
            subscription = False
        else:
            subscription = True
        print('subscription', subscription)
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
    

    dict_query_data = parse_query_data(query_data=query.data)
    if dict_query_data['type'] == 'subs':
        print('type == subs')
        if dict_query_data['subscription'] == True:
            print('subs == True')
            # unsubscribe func
            # FIXME:
        else:
            # subscribe func
            print('subs == False')

            game_prices = find_game_price_by_id(dict_query_data['game_id'])
            subscribe_to_game(chat_id=update.effective_chat.id,
                              game_id=dict_query_data['game_id'],
                              game_price=game_prices[2],
                              game_plus_price=game_prices[3])
            print('subscribed successfully')



    query.edit_message_caption(caption=f"Selected option: {query.data}")