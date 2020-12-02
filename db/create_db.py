from db_utils import (START_DB_NAME, USER, HOST, PASSWORD, ISOLATION_LEVEL_AUTOCOMMIT,
            DB_NAME, psycopg2, execute_sql)


def create_db():
    '''create database psn_db'''
    conn = psycopg2.connect(
        dbname=START_DB_NAME, user=USER, host=HOST, password=PASSWORD)
    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cur = conn.cursor()
    cur.execute(f'CREATE DATABASE {DB_NAME}')
    cur.close()
    conn.close()


# TODO: title is not unique!!! need to find another point
def create_table_games():
    '''create table games'''
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
    execute_sql(sql)
    print('created table games successfully')

# TODO: write a trigger for auto update column 'updated_time'  


if __name__ == '__main__':
    create_db()
    print('db created')
    
    create_table_games()