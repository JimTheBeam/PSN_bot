import psycopg2
from psycopg2.errors import DuplicateDatabase
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

import sys
sys.path.append('..')
from PSN_bot.config import Config


START_DB_NAME = Config.START_DB_NAME
USER = Config.DB_USER
HOST = Config.DB_HOST
PASSWORD = Config.DB_PASSWORD
DB_NAME = Config.DB_NAME