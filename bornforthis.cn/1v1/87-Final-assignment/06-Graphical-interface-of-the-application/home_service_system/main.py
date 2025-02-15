# # main.py
# import tkinter as tk
# from gui.login_page import LoginPage
# from gui.registration_page import RegistrationPage
#
#
# class HomeServiceSystemApp(tk.Tk):
#     def __init__(self):
#         tk.Tk.__init__(self)
#         self.title("家政服务系统")
#         self.geometry("400x300")
#         self.frames = {}
#         self.create_frames()
#
#     def create_frames(self):
#         for F in (LoginPage, RegistrationPage):
#             page_name = F.__name__
#             frame = F(parent=self, controller=self)
#             self.frames[page_name] = frame
#             frame.grid(row=0, column=0, sticky="nsew")
#
#         self.show_frame("LoginPage")
#
#     def show_frame(self, page_name):
#         frame = self.frames[page_name]
#         frame.tkraise()
#
#     def show_home_page(self, user):
#         # 根据用户角色显示相应的主页
#         pass
#
#
# if __name__ == "__main__":
#     app = HomeServiceSystemApp()
#     app.mainloop()
# main.py
import tkinter as tk
from gui.login_page import LoginPage
from gui.registration_page import RegistrationPage
from gui.home_page import HomePage
from gui.admin_page import AdminPage
from gui.employer_page import EmployerPage
from gui.employee_page import EmployeePage


class HomeServiceSystemApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("家政服务系统")
        self.geometry("400x300")
        self.frames = {}
        self.current_user = None
        self.create_frames()

    def create_frames(self):
        for F in (LoginPage, RegistrationPage):
            page_name = F.__name__
            frame = F(parent=self, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("LoginPage")

    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

    def show_home_page(self, user):
        self.current_user = user
        home_page = HomePage(parent=self, controller=self, user=user)
        home_page.grid(row=0, column=0, sticky="nsew")
        self.frames["HomePage"] = home_page
        home_page.tkraise()

        role = user[3]
        if role == "管理员":
            admin_page = AdminPage(parent=self, controller=self)
            admin_page.grid(row=0, column=0, sticky="nsew")
            self.frames["AdminPage"] = admin_page
        elif role == "雇主":
            employer_page = EmployerPage(parent=self, controller=self, user=user)
            employer_page.grid(row=0, column=0, sticky="nsew")
            self.frames["EmployerPage"] = employer_page
        elif role == "雇员":
            employee_page = EmployeePage(parent=self, controller=self, user=user)
            employee_page.grid(row=0, column=0, sticky="nsew")
            self.frames["EmployeePage"] = employee_page


if __name__ == "__main__":
    app = HomeServiceSystemApp()
    app.mainloop()
