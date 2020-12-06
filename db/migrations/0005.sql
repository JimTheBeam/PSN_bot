-- change table user_games. 
DROP table users;


CREATE TABLE users (
    id BIGSERIAL,
    chat_id INTEGER PRIMARY KEY NOT NULL UNIQUE,        
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP);


DROP TABLE user_games;


CREATE TABLE user_games (
    chat_id INTEGER REFERENCES users ON DELETE CASCADE,
    game_id INT REFERENCES games ON DELETE CASCADE,
    created_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    game_price  INTEGER,
    game_plus_price INTEGER,
    CONSTRAINT user_games_primary_key PRIMARY KEY (chat_id, game_id)    
);


UPDATE migration_version SET version = 5;