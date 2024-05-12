import os

from dotenv import load_dotenv

load_dotenv()

USER = os.environ.get('DB_USER')
PASSWORD = os.environ.get('PASSWORD')
DATABASE = os.environ.get('DATABASE')

DATABASE_CONFIG: dict[str, str | None | int] = {
    "database": DATABASE,
    "user": USER,
    "password": PASSWORD,
    "host": "localhost",
    "port":  5432
}

