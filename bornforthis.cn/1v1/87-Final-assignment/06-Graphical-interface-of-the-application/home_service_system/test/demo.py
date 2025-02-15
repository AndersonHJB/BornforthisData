
import tkinter as tk
import tkinter.messagebox as msg
import pickle
import re

def save_user_info(username, password):
    with open('用户信息.pkl', 'wb') as f:
        pickle.dump({'username': username, 'password': password}, f)

def load_user_info():
    try:
        with open('用户信息.pkl', 'rb') as f:
            return pickle.load(f)
    except (FileNotFoundError, EOFError):
        return None

def create_book_info_file():
    # 创建书籍信息文件并初始化一些示例数据
    book_info = """
    《西游记》:作者 :吴承恩
    《红楼梦》:作者:曹雪芹
    《水浒传》:作者:施耐庵
    """
    with open('书籍信息.txt', 'w') as file:
        file.write(book_info)

def user_login():
    login_window = tk.Toplevel()
    login_window.title('用户登录')
    login_window.geometry("280x150")

    tk.Label(login_window, text="用户名:").grid(row=0)
    tk.Label(login_window, text="密码:").grid(row=1)

    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show="*")

    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        user_info = load_user_info()
        if user_info and user_info['username'] == username and user_info['password'] == password:
            login_window.destroy()
            show_user_operations()
        else:
            msg.showwarning("登录失败", "用户名或密码错误")

    tk.Button(login_window, text="登录", command=login).grid(row=2, column=0)
    tk.Button(login_window, text="注册", command=user_register).grid(row=2, column=1)

def user_register():
    register_window = tk.Toplevel()
    register_window.title('用户注册')
    register_window.geometry("280x180")

    tk.Label(register_window, text="用户名:").grid(row=0)
    tk.Label(register_window, text="密码:").grid(row=1)
    tk.Label(register_window, text="确认密码:").grid(row=2)

    new_username_entry = tk.Entry(register_window)
    new_password_entry = tk.Entry(register_window, show="*")
    confirm_password_entry = tk.Entry(register_window, show="*")

    new_username_entry.grid(row=0, column=1)
    new_password_entry.grid(row=1, column=1)
    confirm_password_entry.grid(row=2, column=1)

    def register():
        new_username = new_username_entry.get()
        new_password = new_password_entry.get()
        confirm_password = confirm_password_entry.get()
        if new_password == confirm_password:
            save_user_info(new_username, new_password)
            msg.showinfo("注册成功", "您已成功注册")
            register_window.destroy()
        else:
            msg.showwarning("注册失败", "两次输入的密码不一致")

    tk.Button(register_window, text="注册", command=register).grid(row=3, column=0, columnspan=2)

def show_user_operations():
    def query_book():
        query_window = tk.Toplevel()
        query_window.title('查询图书')
        query_window.geometry("280x100")

        tk.Label(query_window, text="书名:").grid(row=0)
        book_name_entry = tk.Entry(query_window)
        book_name_entry.grid(row=0, column=1)

        def query():
            book_name = book_name_entry.get()
            result = search_book(book_name)
            if result:
                tk.messagebox.showinfo("查询结果", result)
            else:
                tk.messagebox.showwarning("未找到", "未找到该书信息")

        tk.Button(query_window, text="查询", command=query).grid(row=1, column=0, columnspan=2)

    def borrow_book():
        borrow_window = tk.Toplevel()
        borrow_window.title('借阅图书')
        borrow_window.geometry("280x150")

        tk.Label(borrow_window, text="书名:").grid(row=0)
        borrow_book_name_entry = tk.Entry(borrow_window)
        borrow_book_name_entry.grid(row=0, column=1)

        def borrow():
            book_name = borrow_book_name_entry.get()
            result = search_book(book_name)
            if result:
                tk.messagebox.showinfo("借阅成功", "您已成功借阅该书")
                borrow_window.destroy()  # 借阅成功后关闭借阅窗口
                delete_book_info(book_name)  # 删除借阅的图书信息
            else:
                tk.messagebox.showwarning("未找到", "未找到该书信息")

        tk.Button(borrow_window, text="借阅", command=borrow).grid(row=1, column=0, columnspan=2)

    def return_book():
        return_window = tk.Toplevel()
        return_window.title('归还图书')
        return_window.geometry("280x150")

        tk.Label(return_window, text="书名:").grid(row=0)
        return_book_name_entry = tk.Entry(return_window)
        return_book_name_entry.grid(row=0, column=1)

        tk.Label(return_window, text="作者:").grid(row=1)
        return_author_entry = tk.Entry(return_window)
        return_author_entry.grid(row=1, column=1)

        def return_book_action():
            book_name = return_book_name_entry.get()
            author = return_author_entry.get()
            if add_book_info(book_name, author):
                tk.messagebox.showinfo("归还成功", "您已成功归还该书")
                return_window.destroy()
            else:
                tk.messagebox.showwarning("错误", "归还失败")

        tk.Button(return_window, text="归还", command=return_book_action).grid(row=2, column=0, columnspan=2)

    user_window = tk.Toplevel()
    user_window.title('用户操作')
    user_window.geometry("280x360")

    tk.Button(user_window, text='查询图书', width=10, height=2, command=query_book).grid(row=3, column=0)
    tk.Button(user_window, text='借阅图书', width=10, height=2, command=borrow_book).grid(row=4, column=0)
    tk.Button(user_window, text='归还图书', width=10, height=2, command=return_book).grid(row=5, column=0)

def admin():
    def query_stock():
        try:
            with open('书籍信息.txt', 'r') as file:
                content = file.read()
                tk.messagebox.showinfo("库存信息", content)
        except FileNotFoundError:
            tk.messagebox.showwarning("错误", "书籍信息文件未找到")

    def add_book():
        add_window = tk.Toplevel()
        add_window.title('添加图书')
        add_window.geometry("280x150")

        tk.Label(add_window, text="书名:").grid(row=0)
        book_name_entry = tk.Entry(add_window)
        book_name_entry.grid(row=0, column=1)

        tk.Label(add_window, text="作者:").grid(row=1)
        author_entry = tk.Entry(add_window)
        author_entry.grid(row=1, column=1)

        def add_action():
            book_name = book_name_entry.get()
            author = author_entry.get()
            if book_name and author:
                with open('书籍信息.txt', 'a') as file:
                    file.write(f"{book_name}:作者 :{author}\n")
                tk.messagebox.showinfo("添加成功", "图书已成功添加")
                add_window.destroy()
            else:
                tk.messagebox.showwarning("错误", "书名和作者都不能为空")

        tk.Button(add_window, text="添加", command=add_action).grid(row=2, column=0, columnspan=2)

    def delete_book():
        delete_window = tk.Toplevel()
        delete_window.title('删除图书')
        delete_window.geometry("280x100")

        tk.Label(delete_window, text="书名:").grid(row=0)
        delete_book_name_entry = tk.Entry(delete_window)
        delete_book_name_entry.grid(row=0, column=1)

        def delete_action():
            book_name = delete_book_name_entry.get()
            if delete_book_info(book_name):
                tk.messagebox.showinfo("删除成功", "该书已成功删除")
                delete_window.destroy()
            else:
                tk.messagebox.showwarning("未找到", "未找到该书信息，删除失败")

        tk.Button(delete_window, text="删除", command=delete_action).grid(row=1, column=0, columnspan=2)

    admin_window = tk.Toplevel()
    admin_window.title('管理员操作')
    admin_window.geometry("280x310")

    tk.Button(admin_window, text='查询库存', width=10, height=2, command=query_stock).grid(row=3, column=0)
    tk.Button(admin_window, text='添加图书', width=10, height=2, command=add_book).grid(row=4, column=0)
    tk.Button(admin_window, text='删除图书', width=10, height=2, command=delete_book).grid(row=5, column=0)

def admin_login():
    login_window = tk.Toplevel()
    login_window.title('管理员登录')
    login_window.geometry("280x150")

    tk.Label(login_window, text="工号:").grid(row=0)
    tk.Label(login_window, text="密码:").grid(row=1)

    username_entry = tk.Entry(login_window)
    password_entry = tk.Entry(login_window, show="*")

    username_entry.grid(row=0, column=1)
    password_entry.grid(row=1, column=1)

    def login():
        username = username_entry.get()
        password = password_entry.get()
        if username == "1001" and password == "1001123":  # 示例验证
            login_window.destroy()
            admin()
        else:
            msg.showwarning("登录失败", "用户名或密码错误")

    tk.Button(login_window, text="登录", command=login).grid(row=2, column=0)

def search_book(book_name):
    try:
        with open('书籍信息.txt', 'r') as file:
            content = file.read()
            pattern = r'{}:\s*(.*)'.format(re.escape(book_name))
            match = re.search(pattern, content)
            if match:
                return match.group(1)
            else:
                return None
    except FileNotFoundError:
        return "书籍信息文件未找到"

def delete_book_info(book_name):
    try:
        with open('书籍信息.txt', 'r') as file:
            lines = file.readlines()
        with open('书籍信息.txt', 'w') as file:
            for line in lines:
                if book_name not in line:
                    file.write(line)
        return True
    except FileNotFoundError:
        print("书籍信息文件未找到")
        return False

def add_book_info(book_name, author):
    try:
        with open('书籍信息.txt', 'a') as file:
            file.write(f"{book_name}:作者 :{author}\n")
        return True
    except FileNotFoundError:
        print("书籍信息文件未找到")
        return False

create_book_info_file()  # 创建书籍信息文件

root = tk.Tk()
root.title('图书管理系统')
root.geometry("700x260")

theLabel = tk.Label(root, compound=tk.CENTER, fg="white").grid(row=0, column=0)
labe1 = tk.Label(root, text="欢迎来到图书管理系统，请选择用户类型：", font=36).grid(row=0, column=1)

tk.Button(root, text='普通用户', width=10, height=2, command=user_login).grid(row=1, column=1)
tk.Button(root, text='管理员', width=10, height=2, command=admin_login).grid(row=2, column=1)

root.mainloop()


