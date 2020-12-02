from db.db_utils import execute_sql_with_data, fetchone_sql_data


def insert_game_in_games(game):
    """insert a game in table games"""
    sql = '''INSERT INTO games (
        title, current_price, plus_price, old_price, 
        image_link, discount_end_date, psprices_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    data = (game['title'], game['current_price'], game['plus_price'],
            game['old_price'], game['image_link'], game['discount_end_date'],
            game['psprices_url'])
    execute_sql_with_data(sql, data)


def find_game(game_name):
    """find game in table games
       return game data from db"""
    sql = '''SELECT title, current_price, plus_price, old_price, 
             image_link, discount_end_date, psprices_url FROM games WHERE LOWER(title)=LOWER(%s);'''
    data = (game_name,)
    game_data = fetchone_sql_data(sql, data)
    return game_data