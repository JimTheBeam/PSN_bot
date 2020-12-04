import psycopg2


import sys
import os
path_to_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(path_to_parent_dir)

from config import Config


# TODO: add exeptions
def execute_sql(sql):
    '''execute and commit one sql query'''
    conn = psycopg2.connect(
        dbname=Config.DB_NAME, user=Config.DB_USER, host=Config.DB_HOST, password=Config.DB_PASSWORD)
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    cur.close()
    conn.close()


# TODO: add exeptions
def execute_sql_with_data(sql, data):
    '''execute and commit one sql query with data 
    :sql: <str> sql query
    :data: <tuple> data for sql query'''
    conn = psycopg2.connect(
        dbname=Config.DB_NAME, user=Config.DB_USER, host=Config.DB_HOST, password=Config.DB_PASSWORD)
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    cur.close()
    conn.close()


# TODO: add exeptions
def fetchone_sql_data(sql, data):
    '''execute sql query, fetch_one and return it
    :sql: <str> sql query
    :data: <tuple> data for sql query'''
    conn = psycopg2.connect(
        dbname=Config.DB_NAME, user=Config.DB_USER, host=Config.DB_HOST, password=Config.DB_PASSWORD)
    cur = conn.cursor()
    cur.execute(sql, data)
    db_data = cur.fetchone()
    cur.close()
    conn.close()
    return db_data


