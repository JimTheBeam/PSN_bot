import psycopg2

import sys
sys.path.append('..')
from PSN_bot.config import Config


USER = Config.DB_USER
HOST = Config.DB_HOST
PASSWORD = Config.DB_PASSWORD
DB_NAME = Config.DB_NAME


def insert_user(chat_id):
    '''insert chat_id into users table'''
    conn = psycopg2.connect(
        dbname=DB_NAME, user=USER, host=HOST, password=PASSWORD)
    cur = conn.cursor()
    sql = '''INSERT INTO users (chat_id)
    VALUES (%s)
    '''
    cur.execute(sql, (chat_id,))
    conn.commit()
    cur.close()
    conn.close()
    print('sql query went successfully')