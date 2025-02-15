# gui/employer_page.py
import tkinter as tk
from backend.booking_management import get_all_employees, book_employee


class EmployerPage(tk.Frame):
    def __init__(self, parent, controller, user):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="雇主页面").grid(row=0, column=0, pady=10)
        self.employee_listbox = tk.Listbox(self)
        self.employee_listbox.grid(row=1, column=0, pady=10)
        tk.Button(self, text="预约", command=self.book_employee).grid(row=2, column=0, pady=10)
        tk.Button(self, text="返回主页", command=lambda: self.controller.show_frame("HomePage")).grid(row=3, column=0,
                                                                                                      pady=10)
        self.refresh_employees()

    def refresh_employees(self):
        self.employee_listbox.delete(0, tk.END)
        employees = get_all_employees()
        for employee in employees:
            self.employee_listbox.insert(tk.END, employee)

    def book_employee(self):
        selected_employee = self.employee_listbox.get(tk.ACTIVE)
        if selected_employee:
            success = book_employee(self.user[0], selected_employee[0])
            if success:
                tk.messagebox.showinfo("成功", "预约成功")
            else:
                tk.messagebox.showerror("错误", "预约失败")
