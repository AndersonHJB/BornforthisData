# # gui/login_page.py
# import tkinter as tk
# from tkinter import messagebox
# from backend.user_management import login_user
#
#
# class LoginPage(tk.Frame):
#     def __init__(self, parent, controller):
#         tk.Frame.__init__(self, parent)
#         self.controller = controller
#         self.create_widgets()
#
#     def create_widgets(self):
#         tk.Label(self, text="用户名").grid(row=0, column=0, pady=10)
#         self.username_entry = tk.Entry(self)
#         self.username_entry.grid(row=0, column=1, pady=10)
#
#         tk.Label(self, text="密码").grid(row=1, column=0, pady=10)
#         self.password_entry = tk.Entry(self, show='*')
#         self.password_entry.grid(row=1, column=1, pady=10)
#
#         tk.Button(self, text="登录", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
#
#     def login(self):
#         username = self.username_entry.get()
#         password = self.password_entry.get()
#         user = login_user(username, password)
#         if user:
#             self.controller.show_home_page(user)
#         else:
#             messagebox.showerror("错误", "用户名或密码错误")
# gui/login_page.py
import tkinter as tk
from tkinter import messagebox
from backend.user_management import login_user


class LoginPage(tk.Frame):
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

        tk.Button(self, text="登录", command=self.login).grid(row=2, column=0, columnspan=2, pady=10)
        tk.Button(self, text="注册", command=lambda: self.controller.show_frame("RegistrationPage")).grid(row=3,
                                                                                                          column=0,
                                                                                                          columnspan=2,
                                                                                                          pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        user = login_user(username, password)
        if user:
            self.controller.show_home_page(user)
        else:
            messagebox.showerror("错误", "用户名或密码错误")
