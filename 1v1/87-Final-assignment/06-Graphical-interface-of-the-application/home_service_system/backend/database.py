# # # backend/database.py
# # import sqlite3
# #
# #
# # def create_connection():
# #     conn = sqlite3.connect('home_service_system.db')
# #     return conn
# #
# #
# # def create_tables():
# #     conn = create_connection()
# #     cursor = conn.cursor()
# #
# #     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
# #                         id INTEGER PRIMARY KEY AUTOINCREMENT,
# #                         username TEXT NOT NULL UNIQUE,
# #                         password TEXT NOT NULL,
# #                         role TEXT NOT NULL)''')
# #     conn.commit()
# #     conn.close()
# #
# #
# # if __name__ == '__main__':
# #     create_tables()
# # backend/database.py
# import sqlite3
#
#
# def create_connection():
#     conn = sqlite3.connect('home_service_system.db')
#     return conn
#
#
# def create_tables():
#     conn = create_connection()
#     cursor = conn.cursor()
#
#     cursor.execute('''CREATE TABLE IF NOT EXISTS users (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         username TEXT NOT NULL UNIQUE,
#                         password TEXT NOT NULL,
#                         role TEXT NOT NULL)''')
#
#     cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT,
#                         employer_id INTEGER NOT NULL,
#                         employee_id INTEGER NOT NULL,
#                         status TEXT NOT NULL,
#                         FOREIGN KEY (employer_id) REFERENCES users(id),
#                         FOREIGN KEY (employee_id) REFERENCES users(id))''')
#
#     conn.commit()
#     conn.close()
#
#
# if __name__ == '__main__':
#     create_tables()
# backend/database.py
import sqlite3
from config import DATABASE_NAME


def create_connection():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn


def create_tables():
    conn = create_connection()
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        username TEXT NOT NULL UNIQUE,
                        password TEXT NOT NULL,
                        role TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS bookings (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        employer_id INTEGER NOT NULL,
                        employee_id INTEGER NOT NULL,
                        status TEXT NOT NULL,
                        FOREIGN KEY (employer_id) REFERENCES users(id),
                        FOREIGN KEY (employee_id) REFERENCES users(id))''')

    conn.commit()
    conn.close()


if __name__ == '__main__':
    create_tables()
