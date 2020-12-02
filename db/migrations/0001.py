import sys
import os
path_to_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(path_to_parent_dir)

from db_utils import execute_sql


# create table users
if __name__ == "__main__":
    sql = '''CREATE TABLE users (
        id BIGSERIAL PRIMARY KEY,
        chat_id VARCHAR(150) NOT NULL UNIQUE,        
        created_time TIMESTAMP
        );
        '''
    execute_sql(sql)
    