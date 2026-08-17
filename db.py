import sqlite3
import configparser
import os

config = configparser.ConfigParser()
try:
    with open("./config.ini") as f:
        config.read_file(f)
except FileNotFoundError:
    print("Config file not found, please create a config file.")
    exit()
db_config = config["Database"]
# if no config, it fails.
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

