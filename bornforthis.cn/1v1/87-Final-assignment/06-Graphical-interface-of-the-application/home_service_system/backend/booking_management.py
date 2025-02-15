# backend/booking_management.py
from backend.database import create_connection
import sqlite3
def get_all_bookings():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings")
    bookings = cursor.fetchall()
    conn.close()
    return bookings

def get_all_employees():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE role = '雇员'")
    employees = cursor.fetchall()
    conn.close()
    return employees

def book_employee(employer_id, employee_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO bookings (employer_id, employee_id, status) VALUES (?, ?, ?)", (employer_id, employee_id, '未完成'))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()

def get_bookings_by_employee(employee_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM bookings WHERE employee_id = ? AND status = '未完成'", (employee_id,))
    bookings = cursor.fetchall()
    conn.close()
    return bookings

def complete_booking(booking_id):
    conn = create_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("UPDATE bookings SET status = '已完成' WHERE id = ?", (booking_id,))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    finally:
        conn.close()
