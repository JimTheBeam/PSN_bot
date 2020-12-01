from telegram import (InlineKeyboardButton, InlineKeyboardMarkup,
                     ReplyKeyboardMarkup, ReplyKeyboardRemove)

#TODO: сделать subscribe/unsubscribe
def game_keyboard(psn_link, subscription):
    '''
    :psn_link: str
    return keyboard for a single game
    '''
    psn_button = InlineKeyboardButton('PSN link', url=psn_link)
    # subscription_button = [InlineKeyboardButton]
    keyboard = InlineKeyboardMarkup([[psn_button]])
    return keyboard



# def my_keyboard():
#     keyboard = ReplyKeyboardMarkup([['Play Twenty-one', 'Play TicTacToe'],
#                                     ['Liderboard for 21', 'Liderboard for TicTacToe'],
#                                     ['Help!']],
                                    # resize_keyboard=True)


def error_keyboard():
    button = [[InlineKeyboardButton('Что-то пошло не так', callback_data=0)]]
    keyboard = InlineKeyboardMarkup(button)
    return keyboard
