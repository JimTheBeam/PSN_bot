import psycopg2
from psycopg2.errors import DuplicateDatabase
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

# conn = psycopg2.connect(
#     host='localhost',
#     database='psn_db',
#     user='postgres',
#     password='123')

def create_db():
    conn = psycopg2.connect(
        dbname='postgres', user='postgres', host='localhost', password='123')

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

    cur = conn.cursor()
    db_name = 'psn_db'
    cur.execute(f'CREATE DATABASE {db_name}')

    cur.close()
    conn.close()




if __name__ == "__main__":
    try:
        create_db()
    except DuplicateDatabase:
        print('database already exists')