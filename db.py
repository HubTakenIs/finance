import sqlite3
import configparser
import os

config = configparser.ConfigParser()
config.read("./config.ini")
db_config = config["Database"]

def get_db_conn():
    db = sqlite3.connect(
            os.path.join(
                db_config["Location"],
                db_config["FileName"])
            )
    return db

def setup_db():
    conn = get_db_conn()
    with open("./schema/schema.sql") as f:
        conn.executescript(f.read())
    conn.close()

