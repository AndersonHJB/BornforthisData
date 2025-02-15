# gui/employee_page.py
import tkinter as tk
from backend.booking_management import get_bookings_by_employee, complete_booking


class EmployeePage(tk.Frame):
    def __init__(self, parent, controller, user):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="雇员页面").grid(row=0, column=0, pady=10)
        self.booking_listbox = tk.Listbox(self)
        self.booking_listbox.grid(row=1, column=0, pady=10)
        tk.Button(self, text="完成任务", command=self.complete_booking).grid(row=2, column=0, pady=10)
        tk.Button(self, text="返回主页", command=lambda: self.controller.show_frame("HomePage")).grid(row=3, column=0,
                                                                                                      pady=10)
        self.refresh_bookings()

    def refresh_bookings(self):
        self.booking_listbox.delete(0, tk.END)
        bookings = get_bookings_by_employee(self.user[0])
        for booking in bookings:
            self.booking_listbox.insert(tk.END, booking)

    def complete_booking(self):
        selected_booking = self.booking_listbox.get(tk.ACTIVE)
        if selected_booking:
            success = complete_booking(selected_booking[0])
            if success:
                tk.messagebox.showinfo("成功", "任务已完成")
            else:
                tk.messagebox.showerror("错误", "任务完成失败")
