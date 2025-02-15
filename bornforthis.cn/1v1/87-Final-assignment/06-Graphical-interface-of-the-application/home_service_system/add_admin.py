# add_admin.py
import sqlite3
from backend.utils import hash_password
from config import DATABASE_NAME


def add_admin_user():
    conn = sqlite3.connect(DATABASE_NAME)
    cursor = conn.cursor()

    username = "admin"
    password = hash_password("admin123")
    role = "管理员"

    try:
        cursor.execute("INSERT INTO users (username, password, role) VALUES (?, ?, ?)", (username, password, role))
        conn.commit()
        print("管理员账户已成功添加。")
    except sqlite3.IntegrityError:
        print("用户名已存在。")
    finally:
        conn.close()


if __name__ == '__main__':
    add_admin_user()
