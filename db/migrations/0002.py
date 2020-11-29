from migration_utils import create_table


# create table user_games
if __name__ == "__main__":
    sql = '''CREATE TABLE user_games (
        user_id INT REFERENCES users,
        game_id INT REFERENCES games,        
        created_time TIMESTAMP
        );
        '''
    create_table(sql)