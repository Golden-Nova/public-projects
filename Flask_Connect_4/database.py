#handles sqlite3 connections can creates database

import os
from pathlib import Path
import sqlite3

def db_exists(db_path : Path) -> bool:
    'given a path checks if a database at that path exists'
    return os.path.exists(db_path)

def create_db(db_path : Path) -> None:
    'given a path creates a new database there, and creates the correct tables'

def check_db(db_path : Path) -> bool:
    'given a path checks if they have the correctly formated tables and returns if they do'

def move_db(db_path : Path) -> None:
    'given a path, moves the database to an unoccupied spot in the directory, to make room on the path given'
    old_path = str(db_path)
    index = 1
    while os.path.exists(f'{old_path}_{index}'):
        index += 1
    os.rename(old_path, f'{old_path}_{index}')