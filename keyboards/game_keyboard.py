from telegram import InlineKeyboardButton, InlineKeyboardMarkup
                     

def utf8len(string):
    ''':string: str
    return number of bytes in a string'''
    return len(string.encode('utf-8'))


def subs_callback_data(game_id, subscription):
    ''':game_id: [str] id in database
    :subscription: [boolean] True if user subscribed to a game
    return callback_data for subscription button'''

    data = f'type:subs,game_id:{game_id},subscription:{subscription}'

    # max size of calback_data is 64 bytes
    if utf8len(data) > 64:
        return 'something wrong happened'
    return data


def make_subscription_button(game_id, subscription):
    '''create subscribe/unsubscribe button'''
    if not subscription:
        text = 'Subscribe to know when price went lower'
    else:
        text = 'Unsubscribe'
    callback_data = subs_callback_data(game_id, subscription)
    button = InlineKeyboardButton(text, callback_data=callback_data)
    return button


def game_keyboard(psn_link, subscription, game_id):
    '''
    :psn_link: [str]
    :subscription: [boolean]
    :game_id: [str] id in database
    return keyboard for a single game
    '''
    psn_button = InlineKeyboardButton('PSN link', url=psn_link)

    subs_button = make_subscription_button(game_id, subscription)
    
    keyboard = InlineKeyboardMarkup([[psn_button], [subs_button]])
    return keyboard


