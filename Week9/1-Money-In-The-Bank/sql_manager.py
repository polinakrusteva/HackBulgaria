import sqlite3
from Client import Client
import settings
import hashlib
import create_db

conn = sqlite3.connect(settings.DB_NAME)
cursor = conn.cursor()


def hash_password(password):
    hashed_password = hashlib.sha1(password.encode())
    return hashed_password.hexdigest()


def check_password(hashed_password, user_password):
    hashed = hashlib.sha1(user_password.encode())
    return hashed_password == hashed.hexdigest()


def change_message(new_message, logged_user):
    cursor.execute(settings.UPDATE_MESSAGE)
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    cursor.execute(settings.UPDATE_PASS)
    conn.commit()


def register(username, password):
    if len(password) > 8:
        cursor.execute(settings.INSERT_SQL)
        conn.commit()


def deposit(money):
    cursor.execute(settings.DEPOSIT_SQL)


def login(username, password):
    cursor.execute(settings.SELECT_QUERY)
    user = cursor.fetchone()
    if(user):
        return Client(user[0], user[1], user[2], user[3])
    else:
        return False
