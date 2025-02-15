import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.util.regex.*;
import java.util.Properties;


public class BookManagementSystem extends JFrame {
    // 路径可能需要根据你的实际情况调整
    private static final String BOOKS_FILE = "书籍信息.txt";
    private static final String USER_INFO_FILE = "用户信息.properties";

    // 声明userProperties变量，用于存储用户信息
    private static Properties userProperties = new Properties();

    public BookManagementSystem() {
        setTitle("图书管理系统");
        setSize(700, 260);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLocationRelativeTo(null);

        JPanel panel = new JPanel();
        panel.setLayout(new FlowLayout());

        JLabel welcomeLabel = new JLabel("欢迎来到图书管理系统，请选择用户类型：");
        panel.add(welcomeLabel);

        JButton userButton = new JButton("普通用户");
        userButton.addActionListener(e -> userLogin());
        panel.add(userButton);

        JButton adminButton = new JButton("管理员");
        adminButton.addActionListener(e -> adminLogin());
        panel.add(adminButton);

        add(panel);
        setVisible(true);
    }


    private void userLogin() {
        JFrame loginWindow = new JFrame("用户登录");
        loginWindow.setSize(280, 150);
        loginWindow.setLocationRelativeTo(null);
        loginWindow.setLayout(new GridLayout(3, 2));

        loginWindow.add(new JLabel("用户名:"));
        JTextField usernameEntry = new JTextField();
        loginWindow.add(usernameEntry);

        loginWindow.add(new JLabel("密码:"));
        JPasswordField passwordEntry = new JPasswordField();
        loginWindow.add(passwordEntry);

        JButton loginButton = new JButton("登录");
        loginButton.addActionListener(e -> {
            String username = usernameEntry.getText();
            String password = new String(passwordEntry.getPassword());
            if (checkUserInfo(username, password)) {
                loginWindow.dispose();
                showUserOperations();
            } else {
                JOptionPane.showMessageDialog(loginWindow, "用户名或密码错误", "登录失败", JOptionPane.WARNING_MESSAGE);
            }
        });
        loginWindow.add(loginButton);

        JButton registerButton = new JButton("注册");
        registerButton.addActionListener(e -> userRegister());
        loginWindow.add(registerButton);

        loginWindow.setVisible(true);
    }

    private void userRegister() {
        JFrame registerWindow = new JFrame("用户注册");
        registerWindow.setSize(280, 180);
        registerWindow.setLocationRelativeTo(null);
        registerWindow.setLayout(new GridLayout(4, 2));

        registerWindow.add(new JLabel("用户名:"));
        JTextField newUsernameEntry = new JTextField();
        registerWindow.add(newUsernameEntry);

        registerWindow.add(new JLabel("密码:"));
        JPasswordField newPasswordEntry = new JPasswordField();
        registerWindow.add(newPasswordEntry);

        registerWindow.add(new JLabel("确认密码:"));
        JPasswordField confirmPasswordEntry = new JPasswordField();
        registerWindow.add(confirmPasswordEntry);

        JButton registerButton = new JButton("注册");
        registerButton.addActionListener(e -> {
            String newUsername = newUsernameEntry.getText();
            String newPassword = new String(newPasswordEntry.getPassword());
            String confirmPassword = new String(confirmPasswordEntry.getPassword());
            if (newPassword.equals(confirmPassword)) {
                saveUserInfo(newUsername, newPassword);
                JOptionPane.showMessageDialog(registerWindow, "您已成功注册", "注册成功", JOptionPane.INFORMATION_MESSAGE);
                registerWindow.dispose();
            } else {
                JOptionPane.showMessageDialog(registerWindow, "两次输入的密码不一致", "注册失败", JOptionPane.WARNING_MESSAGE);
            }
        });
        registerWindow.add(registerButton);

        registerWindow.setVisible(true);
    }

    private void showUserOperations() {
        JFrame userWindow = new JFrame("用户操作");
        userWindow.setSize(280, 360);
        userWindow.setLocationRelativeTo(null);
        userWindow.setLayout(new GridLayout(3, 1));

        JButton queryBookButton = new JButton("查询图书");
        queryBookButton.addActionListener(e -> queryBook());
        userWindow.add(queryBookButton);

        JButton borrowBookButton = new JButton("借阅图书");
        borrowBookButton.addActionListener(e -> borrowBook());
        userWindow.add(borrowBookButton);

        JButton returnBookButton = new JButton("归还图书");
        returnBookButton.addActionListener(e -> returnBook());
        userWindow.add(returnBookButton);

        userWindow.setVisible(true);
    }

    private void adminLogin() {
        JFrame loginWindow = new JFrame("管理员登录");
        loginWindow.setSize(280, 150);
        loginWindow.setLocationRelativeTo(null);
        loginWindow.setLayout(new GridLayout(2, 2));

        loginWindow.add(new JLabel("工号:"));
        JTextField usernameEntry = new JTextField();
        loginWindow.add(usernameEntry);

        loginWindow.add(new JLabel("密码:"));
        JPasswordField passwordEntry = new JPasswordField();
        loginWindow.add(passwordEntry);

        JButton loginButton = new JButton("登录");
        loginButton.addActionListener(e -> {
            String username = usernameEntry.getText();
            String password = new String(passwordEntry.getPassword());
            if (username.equals("admin") && password.equals("admin123")) {  // 示例验证
                loginWindow.dispose();
                showAdminOperations();
            } else {
                JOptionPane.showMessageDialog(loginWindow, "用户名或密码错误", "登录失败", JOptionPane.WARNING_MESSAGE);
            }
        });
        loginWindow.add(loginButton);

        loginWindow.setVisible(true);
    }

    private void showAdminOperations() {
        JFrame adminWindow = new JFrame("管理员操作");
        adminWindow.setSize(280, 310);
        adminWindow.setLocationRelativeTo(null);
        adminWindow.setLayout(new GridLayout(3, 1));

        JButton queryStockButton = new JButton("查询库存");
        queryStockButton.addActionListener(e -> queryStock());
        adminWindow.add(queryStockButton);

        JButton addBookButton = new JButton("添加图书");
        addBookButton.addActionListener(e -> addBook());
        adminWindow.add(addBookButton);

        JButton deleteBookButton = new JButton("删除图书");
        deleteBookButton.addActionListener(e -> deleteBook());
        adminWindow.add(deleteBookButton);

        adminWindow.setVisible(true);
    }

    private void queryBook() {
        JFrame queryWindow = new JFrame("查询图书");
        queryWindow.setSize(280, 100);
        queryWindow.setLocationRelativeTo(null);
        queryWindow.setLayout(new GridLayout(2, 2));

        queryWindow.add(new JLabel("书名:"));
        JTextField bookNameEntry = new JTextField();
        queryWindow.add(bookNameEntry);

        JButton queryButton = new JButton("查询");
        queryButton.addActionListener(e -> {
            String bookName = bookNameEntry.getText();
            String result = searchBook(bookName);
            if (result != null) {
                JOptionPane.showMessageDialog(queryWindow, result, "查询结果", JOptionPane.INFORMATION_MESSAGE);
            } else {
                JOptionPane.showMessageDialog(queryWindow, "未找到该书信息", "未找到", JOptionPane.WARNING_MESSAGE);
            }
        });
        queryWindow.add(queryButton);

        queryWindow.setVisible(true);
    }

    private void borrowBook() {
        JFrame borrowWindow = new JFrame("借阅图书");
        borrowWindow.setSize(280, 150);
        borrowWindow.setLocationRelativeTo(null);
        borrowWindow.setLayout(new GridLayout(2, 2));

        borrowWindow.add(new JLabel("书名:"));
        JTextField borrowBookNameEntry = new JTextField();
        borrowWindow.add(borrowBookNameEntry);

        JButton borrowButton = new JButton("借阅");
        borrowButton.addActionListener(e -> {
            String bookName = borrowBookNameEntry.getText();
            String result = searchBook(bookName);
            if (result != null) {
                deleteBookInfo(bookName); // 删除书籍信息表示借出
                JOptionPane.showMessageDialog(borrowWindow, "您已成功借阅该书", "借阅成功", JOptionPane.INFORMATION_MESSAGE);
                borrowWindow.dispose();
            } else {
                JOptionPane.showMessageDialog(borrowWindow, "未找到该书信息", "未找到", JOptionPane.WARNING_MESSAGE);
            }
        });
        borrowWindow.add(borrowButton);

        borrowWindow.setVisible(true);
    }

    private void returnBook() {
        JFrame returnWindow = new JFrame("归还图书");
        returnWindow.setSize(280, 150);
        returnWindow.setLocationRelativeTo(null);
        returnWindow.setLayout(new GridLayout(3, 2));

        returnWindow.add(new JLabel("书名:"));
        JTextField returnBookNameEntry = new JTextField();
        returnWindow.add(returnBookNameEntry);

        returnWindow.add(new JLabel("作者:"));
        JTextField returnAuthorEntry = new JTextField();
        returnWindow.add(returnAuthorEntry);

        JButton returnButton = new JButton("归还");
        returnButton.addActionListener(e -> {
            String bookName = returnBookNameEntry.getText();
            String author = returnAuthorEntry.getText();
            addBookInfo(bookName, author);
            JOptionPane.showMessageDialog(returnWindow, "您已成功归还该书", "归还成功", JOptionPane.INFORMATION_MESSAGE);
            returnWindow.dispose();
        });
        returnWindow.add(returnButton);

        returnWindow.setVisible(true);
    }

    private void queryStock() {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(BOOKS_FILE));
            String line;
            StringBuilder content = new StringBuilder();
            while ((line = reader.readLine()) != null) {
                content.append(line).append("\n");
            }
            reader.close();
            JOptionPane.showMessageDialog(this, content.toString(), "库存信息", JOptionPane.INFORMATION_MESSAGE);
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "书籍信息文件未找到", "错误", JOptionPane.WARNING_MESSAGE);
        }
    }

    private void addBook() {
        JFrame addWindow = new JFrame("添加图书");
        addWindow.setSize(280, 150);
        addWindow.setLocationRelativeTo(null);
        addWindow.setLayout(new GridLayout(3, 2));

        addWindow.add(new JLabel("书名:"));
        JTextField bookNameEntry = new JTextField();
        addWindow.add(bookNameEntry);

        addWindow.add(new JLabel("作者:"));
        JTextField authorEntry = new JTextField();
        addWindow.add(authorEntry);

        JButton addButton = new JButton("添加");
        addButton.addActionListener(e -> {
            String bookName = bookNameEntry.getText();
            String author = authorEntry.getText();
            if (!bookName.isEmpty() && !author.isEmpty()) {
                try {
                    BufferedWriter writer = new BufferedWriter(new FileWriter(BOOKS_FILE, true));
                    writer.write(bookName + ":作者 :" + author + "\n");
                    writer.close();
                    JOptionPane.showMessageDialog(addWindow, "图书已成功添加", "添加成功", JOptionPane.INFORMATION_MESSAGE);
                    addWindow.dispose();
                } catch (IOException ex) {
                    JOptionPane.showMessageDialog(addWindow, "添加图书失败", "错误", JOptionPane.WARNING_MESSAGE);
                }
            } else {
                JOptionPane.showMessageDialog(addWindow, "书名和作者都不能为空", "错误", JOptionPane.WARNING_MESSAGE);
            }
        });
        addWindow.add(addButton);

        addWindow.setVisible(true);
    }

    private void deleteBook() {
        JFrame deleteWindow = new JFrame("删除图书");
        deleteWindow.setSize(280, 100);
        deleteWindow.setLocationRelativeTo(null);
        deleteWindow.setLayout(new GridLayout(2, 2));

        deleteWindow.add(new JLabel("书名:"));
        JTextField deleteBookNameEntry = new JTextField();
        deleteWindow.add(deleteBookNameEntry);

        JButton deleteButton = new JButton("删除");
        deleteButton.addActionListener(e -> {
            String bookName = deleteBookNameEntry.getText();
            if (deleteBookInfo(bookName)) {
                JOptionPane.showMessageDialog(deleteWindow, "该书已成功删除", "删除成功", JOptionPane.INFORMATION_MESSAGE);
                deleteWindow.dispose();
            } else {
                JOptionPane.showMessageDialog(deleteWindow, "未找到该书信息，删除失败", "未找到", JOptionPane.WARNING_MESSAGE);
            }
        });
        deleteWindow.add(deleteButton);

        deleteWindow.setVisible(true);
    }

    private String searchBook(String bookName) {
        try {
            BufferedReader reader = new BufferedReader(new FileReader(BOOKS_FILE));
            String line;
            Pattern pattern = Pattern.compile(bookName + ":\\s*(.*)");
            while ((line = reader.readLine()) != null) {
                Matcher matcher = pattern.matcher(line);
                if (matcher.find()) {
                    reader.close();
                    return matcher.group(1);
                }
            }
            reader.close();
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "书籍信息文件未找到", "错误", JOptionPane.WARNING_MESSAGE);
        }
        return null;
    }

    private boolean deleteBookInfo(String bookName) {
        try {
            File inputFile = new File(BOOKS_FILE);
            File tempFile = new File(inputFile.getAbsolutePath() + ".tmp");

            BufferedReader reader = new BufferedReader(new FileReader(inputFile));
            BufferedWriter writer = new BufferedWriter(new FileWriter(tempFile));

            String line;
            boolean found = false;

            while ((line = reader.readLine()) != null) {
                String trimmedLine = line.trim();
                if (!trimmedLine.startsWith(bookName)) {
                    writer.write(line + System.getProperty("line.separator"));
                } else {
                    found = true;
                }
            }
            writer.close();
            reader.close();

            if (!found) {
                tempFile.delete();
                return false;
            }

            if (!inputFile.delete()) {
                JOptionPane.showMessageDialog(this, "无法删除原文件", "错误", JOptionPane.ERROR_MESSAGE);
                return false;
            }
            if (!tempFile.renameTo(inputFile)) {
                JOptionPane.showMessageDialog(this, "无法重命名临时文件", "错误", JOptionPane.ERROR_MESSAGE);
                return false;
            }

            return true;
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "文件操作失败", "错误", JOptionPane.ERROR_MESSAGE);
            return false;
        }
    }

    private void addBookInfo(String bookName, String author) {
        try {
            BufferedWriter writer = new BufferedWriter(new FileWriter(BOOKS_FILE, true));
            writer.write(bookName + ":作者 :" + author + "\n");
            writer.close();
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "无法添加图书信息", "错误", JOptionPane.ERROR_MESSAGE);
        }
    }

    private boolean checkUserInfo(String username, String password) {
        try {
            userProperties.load(new FileInputStream(USER_INFO_FILE));
            String storedPassword = userProperties.getProperty(username);
            return storedPassword != null && storedPassword.equals(password);
        } catch (IOException e) {
            return false;
        }
    }

    private void saveUserInfo(String username, String password) {
        try {
            userProperties.setProperty(username, password);
            userProperties.store(new FileOutputStream(USER_INFO_FILE), "User Credentials");
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "无法保存用户信息", "错误", JOptionPane.ERROR_MESSAGE);
        }
    }


    public static void main(String[] args) {

        new BookManagementSystem();
    }
}




