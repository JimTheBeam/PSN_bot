import psycopg2
from psycopg2.errors import DuplicateDatabase
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import sys
sys.path.append('..')
from PSN_bot.config import Config


START_DB_NAME = Config.START_DB_NAME
USER = Config.DB_USER
HOST = Config.DB_HOST
PASSWORD = Config.DB_PASSWORD
DB_NAME = Config.DB_NAME


def create_db():
    '''create database psn_db'''
    conn = psycopg2.connect(
        dbname=START_DB_NAME, user=USER, host=HOST, password=PASSWORD)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(f'CREATE DATABASE {DB_NAME}')
    cur.close()
    conn.close()


# TODO: game id is not unique need to find another point
def create_table_games():
    '''create table games'''
    conn = psycopg2.connect(
        dbname=DB_NAME, user=USER, host=HOST, password=PASSWORD)
    cur = conn.cursor()
    sql = '''CREATE TABLE games (
        game_id BIGSERIAL PRIMARY KEY,
        title VARCHAR(150) NOT NULL,
        current_price VARCHAR(50),
        plus_price VARCHAR(50),
        old_price VARCHAR(50),
        image_link VARCHAR(200) NOT NULL,
        discount_end_date VARCHAR(50),
        psprices_url VARCHAR(200) UNIQUE,
        created_time TIMESTAMP,
        updated_time TIMESTAMP
        );
        '''
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()
    print('created table games successfully')

# TODO: write a trigger for auto update column 'updated_time'  


if __name__ == '__main__':
    try:
        create_db()
        print('created db')
    except DuplicateDatabase:
        print('database already exists')
    
    create_table_games()