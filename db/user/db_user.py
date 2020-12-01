import psycopg2

import sys
sys.path.append('..')
from PSN_bot.config import Config


USER = Config.DB_USER
HOST = Config.DB_HOST
PASSWORD = Config.DB_PASSWORD
DB_NAME = Config.DB_NAME


def insert_user_data(chat_id):
    '''insert chat_id into users table'''
    conn = psycopg2.connect(
        dbname=DB_NAME, user=USER, host=HOST, password=PASSWORD)
    cur = conn.cursor()
    sql = '''INSERT INTO users (chat_id)
    VALUES (%s)
    ON CONFLICT DO NOTHING;
    '''
    cur.execute(sql, (chat_id,))
    conn.commit()
    cur.close()
    conn.close()


def is_user_subscribed_game(chat_id, game_name):
    '''check if user subscribed to a game'''
    conn = psycopg2.connect(
        dbname=DB_NAME, user=USER, host=HOST, password=PASSWORD)
    cur = conn.cursor()

    sql = '''SELECT user_id FROM user_games 
    WHERE user_id = (SELECT id FROM users WHERE chat_id = %s)
    AND 
    game_id = (SELECT game_id FROM games WHERE title = %s);'''

    cur.execute(sql, (str(chat_id), game_name))
    cur.fetchone()
    cur.close()
    conn.close()