import sys
import os
path_to_parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
sys.path.append(path_to_parent_dir)

from db_utils import execute_sql


# create table user_games
if __name__ == "__main__":
    sql = '''CREATE TABLE user_games (
        user_id INT REFERENCES users (id) ON DELETE CASCADE,
        game_id INT REFERENCES games ON DELETE CASCADE,        
        created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        '''
    execute_sql(sql)