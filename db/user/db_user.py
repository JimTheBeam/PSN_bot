from db.db_utils import execute_sql_with_data, fetchone_sql_data


def insert_user_data(chat_id):
    '''insert chat_id into users table'''
    
    sql = '''INSERT INTO users (chat_id)
    VALUES (%s)
    ON CONFLICT DO NOTHING;
    '''
    data = (chat_id,)
    execute_sql_with_data(sql, data)


def is_user_subscribed_game(chat_id, game_id):
    '''check if user subscribed to a game'''

    sql = '''SELECT user_id FROM user_games 
    WHERE user_id = (SELECT id FROM users WHERE chat_id = %s)
    AND 
    game_id = %s;
    '''
    data = (str(chat_id), game_id)
    subscription = execute_sql_with_data(sql, data)
    return subscription


def subscribe_to_game(chat_id, game_id):
    '''subscribe user to a game'''
    sql = '''INSERT INTO user_games (
        user_id, game_id, game_price, game_plus_price)
        VALUES (%s, %s, %s, %s)'''
    
    data = (user_id, game_id, game_price, game_plus_price)

    execute_sql_with_data(sql, data)
    
