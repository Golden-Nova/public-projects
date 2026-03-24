#handles sqlite3 connections can creates database

import os
from pathlib import Path
import sqlite3
from collections.abc import Generator

def db_exists(db_path : Path) -> bool:
    'given a path checks if a database at that path exists'
    return os.path.exists(db_path)

def create_db(db_path : Path) -> None:
    'given a path creates a new database there, and creates the correct tables'
    commands = Path(__file__).absolute().parent / 'connect_schema.sql'
    with open(commands, 'rt') as schema:
        statements = schema.read().split('--')
    conn = Connection(db_path)
    for statement in statements:
        conn.execute_query(statement)
    conn.close()

def check_db(db_path : Path) -> bool:
    'given a path checks if they have the correctly formatted tables and returns if they do'
    conn = Connection(db_path)
    table_names = [result[0] for result in conn.execute_query("SELECT name FROM sqlite_master WHERE type='table' AND name IN ('player', 'games')")]
    player_columns = [conn.execute_query("PRAGMA table_info(player)")]
    games_columns = [conn.execute_query("PRAGMA table_info(games)")]
    conn.close()
    return table_names == ['player', 'games'] and \
            player_columns == [[(0, 'user_id', 'INTEGER', 1, None, 1), (1, 'username', 'TEXT', 1, None, 0), (2, 'password', 'TEXT', 1, None, 0), (3, 'past_ai_wins', 'INTEGER', 1, None, 0), (4, 'past_ai_losses', 'INTEGER', 1, None, 0), (5, 'past_multi_wins', 'INTEGER', 1, None, 0), (6, 'past_multi_losses', 'INTEGER', 1, None, 0)]] and \
            games_columns == [[(0, 'game_id', 'INTEGER', 1, None, 1), (1, 'game_type', 'TEXT', 1, None, 0), (2, 'red_player_id', 'TEXT', 0, None, 0), (3, 'yellow_player_id', 'TEXT', 0, None, 0), (4, 'game', 'BLOB', 1, None, 0)]]

def move_db(db_path : Path) -> str:
    'given a path, moves the database to an unoccupied spot in the directory, to make room on the path given'
    old_path = str(db_path)
    index = 1
    while os.path.exists(f'{old_path}_{index}'):
        index += 1
    os.rename(old_path, f'{old_path}_{index}')
    return f'{old_path}_{index}'

def startup_connection() -> Connection:
    """creates a connection to a connect.db file in the current directory, making one if it doesn't exists and move if if it does not"""
    db_path = Path(__file__).absolute().parent / 'connect.db'
    print('checking for database...           ', end = '')
    if db_exists(db_path):
        print('database found')
        print('checking database validity...      ', end = '')
        if check_db(db_path):
            print('database valid')
        else:
            print('database invalid')
            print('moving database and creating a new database')
            print(f'database moved to {move_db(db_path)}')
            print('creating new database')
            create_db(db_path)
    else:
        print('database not found')
        print('creating new database')
        create_db(db_path)
    print('connecting to database')
    conn = Connection(db_path)
    return conn

class Connection:
    def __init__(self, path : Path):
        """a python object that connects to a database and manages queries"""
        try:
            self._connection = sqlite3.connect(database = path)
            self.status = True
        except sqlite3.OperationalError or sqlite3.DatabaseError as error:
            self.status = False
            raise FileNotFoundError(f'database error: {error}')

    def execute_query(self, statement : str, parameters : dict = {}) -> list[tuple]:
        if self.status:
            try:
                cursor = self._connection.execute(statement, parameters)
                return cursor.fetchall()
            finally:
                if 'cursor' in locals():
                    self._connection.commit()
                    cursor.close()
        else:
            raise RuntimeError("Attempted to execute a query on a connection that is not connected")

    def close(self):
        """closes the db connection if it exists"""
        if self.status:
            self._connection.close()

    def __del__(self):
        'closes the database connection when connection is deleted, if it is not already closed'
        self.close()