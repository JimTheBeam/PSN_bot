from telegram import (InlineKeyboardButton, InlineKeyboardMarkup,
                     ReplyKeyboardMarkup, ReplyKeyboardRemove)


def game_keyboard(psn_link, subscription):
    '''
    :psn_link: str
    :subscription: boolean
    return keyboard for a single game
    '''
    psn_button = InlineKeyboardButton('PSN link', url=psn_link)

    if not subscription:
        text = 'Subscribe to know when price went lower'
        callback_data = 1
    else:
        text = 'Unsubscribe'
        callback_data = 0
    subscription_button = InlineKeyboardButton(text, callback_data=callback_data)

    keyboard = InlineKeyboardMarkup([[psn_button], [subscription_button]])
    return keyboard


