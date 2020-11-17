import psycopg2

import sys
sys.path.append('..')
from PSN_bot.config import Config


USER = Config.DB_USER
HOST = Config.DB_HOST
PASSWORD = Config.DB_PASSWORD
DB_NAME = Config.DB_NAME


def insert_game_in_games(game):
    """insert a game in table games"""
    conn = psycopg2.connect(
        dbname=DB_NAME, user=USER, host=HOST, password=PASSWORD)
    cur = conn.cursor()

    sql = '''INSERT INTO games (
        title, current_price, plus_price, old_price, 
        image_link, discount_end_date, psprices_url)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    '''
    data = (game['title'], game['current_price'], game['plus_price'],
            game['old_price'], game['image_link'], game['discount_end_date'],
            game['psprices_url'])

    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()