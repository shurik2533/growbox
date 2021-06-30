import mysql.connector
from datetime import datetime

from config.db import USER, PASSWORD, DATABASE, HOST, PORT


def save_state_to_db(state_string):
    with mysql.connector.connect(user=USER, password=PASSWORD, database=DATABASE, host=HOST, port=PORT) as conn:
        cursor = conn.cursor()
        query = 'INSERT INTO log (ts, log) VALUES (%s, %s)'
        cursor.execute(query, (datetime.now(), state_string))
        conn.commit()
