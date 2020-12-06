from db.user.db_user import is_user_subscribed_game


def convert_game_tuple_to_dict(game):
    '''create and return a dict from tuple for a single game
    :game: [list] data from database about certain game:
            [0] game_id
            [1] title
            [2] current_price
            [3] plus_price
            [4] old_price 
            [5] image_link
            [6] discount_end_date
            [7] psprices_url
            '''
    dict_game = {}
    dict_game['game_id'] = game[0]
    dict_game['title'] = game[1]
    dict_game['current_price'] = game[2]
    dict_game['plus_price'] = game[3]
    dict_game['old_price'] = game[4]
    dict_game['image_link'] = game[5]
    dict_game['discount_end_date'] = game[6]
    dict_game['psprices_url'] = game[7]
    return dict_game


def create_game_text(game: dict, currency='₽'):
    '''create game text for user using game data from database
    formats text as markdownV2 style:
            *bold text*
            _italic text_
            __underline__
            ~strikethrough~
    :game: [dict] data from database about certain game:
    :return: text about game'''
    game_title = game['title']
    if game_title is None:
        game_title = ''
    else:
        game_title = f'*{game_title}*\n'
    
    current_game_price = game['current_price']
    if current_game_price is None:
        current_game_price = ''
    else:
        current_game_price = f'Current price: *_{current_game_price}{currency}_*\n'
    
    plus_price = game['plus_price']
    if plus_price is None:
        plus_price = ''
    else:
        plus_price = f'PS Plus price: *_{plus_price}{currency}_*\n'
    
    old_price = game['old_price']
    if old_price is None:
        old_price = ''
    else:
        old_price = f'Old price: ~{old_price}{currency}~\n'
    
    discount_end_date = game['discount_end_date']
    if discount_end_date is None:
        discount_end_date = ''
    else:
        discount_end_date = f'_{discount_end_date}_\n'.replace('.', '\.')
    
    game_text = game_title + current_game_price + plus_price + old_price + discount_end_date
    return game_text


# TODO: доработать функцию. нужно чтобы она парсила остальные случаи, когда тип не subs!
def parse_query_data(query_data:str):
    '''parse query data
    :query_data: "type:subs,game_id:{game_id},subscription:{Boolean}"
    :return: dict of query_data'''
    query_data_type = query_data.split('type:')[1].split(',')[0]

    if query_data_type == 'subs':
        game_id = query_data.split('game_id:')[1].split(',')[0]
        subscription = query_data.split('subscription:')[1]
        return {'type': 'subs', 'game_id': game_id, 'subscription':subscription}
    return None
    

def get_subscription_status(chat_id, game_id):
    '''check if user subscribed to a game
    :return: True if subscribed else False
    '''
    subscription = is_user_subscribed_game(
                                chat_id=chat_id,
                                game_id=game_id)
    if subscription is None:
        return False
    else:
        return True