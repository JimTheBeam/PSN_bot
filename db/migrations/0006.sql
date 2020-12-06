-- change price type in table games to INTEGER
ALTER TABLE games
DROP COLUMN current_price,
DROP COLUMN plus_price,
DROP COLUMN old_price;


ALTER TABLE games
ADD COLUMN current_price INTEGER,
ADD COLUMN plus_price INTEGER,
ADD COLUMN old_price INTEGER;


UPDATE migration_version SET version = 6;