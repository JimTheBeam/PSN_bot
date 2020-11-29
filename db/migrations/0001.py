from migration_utils import create_table


# create table users
if __name__ == "__main__":
    sql = '''CREATE TABLE users (
        id BIGSERIAL PRIMARY KEY,
        chat_id VARCHAR(150) NOT NULL UNIQUE,        
        created_time TIMESTAMP
        );
        '''
    create_table(sql)
    