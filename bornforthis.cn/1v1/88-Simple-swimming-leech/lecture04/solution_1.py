def main():
    # 请求用户输入第一个整数
    x_input = input("Please enter an integer >= 10: ")
    # 检查输入是否为数字，并且是非负数
    if not x_input.isdigit():
        print("Invalid number!")
        return
    x = int(x_input)
    if x < 10:
        print("Too small!")
        return
    # 请求用户输入第二个整数
    y_input = input("Please enter an integer >= 10: ")
    # 检查输入是否为数字，并且是非负数
    if not y_input.isdigit():
        print("Invalid number!")
        return
    y = int(y_input)
    if y < 10:
        print("Too small!")
        return
    print(f"{x} + {y} = {x + y}")


if __name__ == "__main__":
    main()
