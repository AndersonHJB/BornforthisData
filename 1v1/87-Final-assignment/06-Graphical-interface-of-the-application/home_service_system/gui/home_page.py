# gui/home_page.py
import tkinter as tk

class HomePage(tk.Frame):
    def __init__(self, parent, controller, user):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.user = user
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text=f"欢迎, {self.user[1]}!").grid(row=0, column=0, pady=10)
        tk.Button(self, text="查看信息", command=self.view_info).grid(row=1, column=0, pady=10)
        tk.Button(self, text="注销", command=self.logout).grid(row=2, column=0, pady=10)

    def view_info(self):
        role = self.user[3]
        if role == "管理员":
            self.controller.show_frame("AdminPage")
        elif role == "雇主":
            self.controller.show_frame("EmployerPage")
        elif role == "雇员":
            self.controller.show_frame("EmployeePage")

    def logout(self):
        self.controller.show_frame("LoginPage")
