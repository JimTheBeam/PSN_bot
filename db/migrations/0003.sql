AlTER TABLE user_games 
ADD CONSTRAINT user_games_primary_key PRIMARY KEY (user_id, game_id);
AlTER TABLE user_games ADD game_price  INTEGER;
AlTER TABLE user_games ADD game_plus_price INTEGER;