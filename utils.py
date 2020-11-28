def create_game_text(game):
    """create game text for user using data from database
    formats text as markdownV2 style:
            *bold text*
            _italic text_
            __underline__
            ~strikethrough~
    :game: [list] data from database about certain game:
            [0] title
            [1] current_price
            [2] plus_price
            [3] old_price 
            [4] image_link
            [5] discount_end_date
            [6] psprices_url
    :return: text about game"""
    if game[0] is None:
        game_title = ''
    else:
        game_title = f'*{game[0]}*\n'
    
    if game[1] is None:
        current_game_price = ''
    else:
        current_game_price = f'Current price: *_{game[1]}_*\n'
    
    if game[2] is None:
        plus_price = ''
    else:
        plus_price = f'PS Plus price: *_{game[2]}_*\n'
    
    if game[3] is None:
        old_price = ''
    else:
        old_price = f'Old price: ~{game[3]}~\n'
    
    if game[5] is None:
        discount_end_date = ''
    else:
        discount_end_date = f'_{game[5]}_\n'.replace('.', '\.')
    
    game_text = game_title + current_game_price + plus_price + old_price + discount_end_date
    return game_text


