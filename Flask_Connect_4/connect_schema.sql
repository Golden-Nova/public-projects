CREATE TABLE player (
    user_id INTEGER NOT NULL PRIMARY KEY,
    username TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    past_ai_wins INTEGER NOT NULL,
    past_ai_losses INTEGER NOT NULL,
    past_multi_wins INTEGER NOT NULL,
    past_multi_losses INTEGER NOT NULL
) STRICT;
--
CREATE TABLE games (
    game_id INTEGER NOT NULL PRIMARY KEY,
    game_type TEXT NOT NULL,
    red_player_id TEXT,
    yellow_player_id TEXT,
    yellow_player_name TEXT,
    red_player_name TEXT,
    board BLOB,
    turn INTEGER,
    winner INTEGER
) STRICT;