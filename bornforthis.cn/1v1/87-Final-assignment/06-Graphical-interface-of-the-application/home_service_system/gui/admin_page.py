# gui/admin_page.py
import tkinter as tk
from backend.booking_management import get_all_bookings


class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self, text="管理员页面").grid(row=0, column=0, pady=10)
        self.booking_listbox = tk.Listbox(self)
        self.booking_listbox.grid(row=1, column=0, pady=10)
        tk.Button(self, text="刷新", command=self.refresh_bookings).grid(row=2, column=0, pady=10)
        tk.Button(self, text="返回主页", command=lambda: self.controller.show_frame("HomePage")).grid(row=3, column=0,
                                                                                                      pady=10)
        self.refresh_bookings()

    def refresh_bookings(self):
        self.booking_listbox.delete(0, tk.END)
        bookings = get_all_bookings()
        for booking in bookings:
            self.booking_listbox.insert(tk.END, booking)
