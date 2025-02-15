# # backend/user_management.py
# from backend.database import create_connection
# import sqlite3
#
# def register_user(username, password, role):
#     conn = create_connection()
#     cursor = conn.cursor()
#     try:
#         cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
#         conn.commit()
#         return True
#     except sqlite3.IntegrityError:
#         return False
#     finally:
#         conn.close()
#
#
# def login_user(username, password):
#     conn = create_connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
#     user = cursor.fetchone()
#     conn.close()
#     return user
# backend/user_management.py
from backend.database import create_connection
from backend.utils import hash_password
import sqlite3


def register_user(username, password, role):
    conn = create_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)",
                       (username, hashed_password, role))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()


def login_user(username, password):
    conn = create_connection()
    cursor = conn.cursor()
    hashed_password = hash_password(password)
    cursor.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, hashed_password))
    user = cursor.fetchone()
    conn.close()
    return user
