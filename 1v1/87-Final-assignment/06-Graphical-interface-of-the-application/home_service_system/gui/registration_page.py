# gui/registration_page.py
import tkinter as tk
from tkinter import messagebox
from backend.user_management import register_user


class RegistrationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="用户名").grid(row=0, column=0, pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.grid(row=0, column=1, pady=10)

        tk.Label(self, text="密码").grid(row=1, column=0, pady=10)
        self.password_entry = tk.Entry(self, show='*')
        self.password_entry.grid(row=1, column=1, pady=10)

        tk.Label(self, text="角色").grid(row=2, column=0, pady=10)
        self.role_var = tk.StringVar(value="雇主")
        tk.OptionMenu(self, self.role_var, "雇主", "雇员").grid(row=2, column=1, pady=10)

        tk.Button(self, text="注册", command=self.register).grid(row=3, column=0, columnspan=2, pady=10)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_var.get()
        success = register_user(username, password, role)
        if success:
            messagebox.showinfo("成功", "注册成功")
            self.controller.show_login_page()
        else:
            messagebox.showerror("错误", "用户名已存在")
