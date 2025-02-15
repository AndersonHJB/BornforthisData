def main():
    input_number = input("Enter an integer between 1 and 20, inclusive: ")

    # 检查输入是否为数字，并且在1到20之间
    if not input_number.isdigit():
        print("Invalid number!")
        return

    # 将输入转换为整数
    number = int(input_number)

    # 检查数字是否在1到20之间
    if not 1 <= number <= 20:
        print("Invalid number!")
        return

    # 打印 "Hello world!" 对应次数
    for _ in range(number):
        print("Hello world!")

    # 如果数字大于5，额外打印 "Phew!"
    if number > 5:
        print("Phew!")


if __name__ == "__main__":
    main()
