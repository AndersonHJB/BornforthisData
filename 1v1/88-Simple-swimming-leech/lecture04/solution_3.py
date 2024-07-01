import datetime


def calculate_age(birthdate):
    today = datetime.date.today()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age


def is_valid_date(date_str):
    # 检查字符串是否为10个字符长度，并且包含两个斜杠
    if len(date_str) != 10 or date_str[4] != '/' or date_str[7] != '/':
        return False

    parts = date_str.split('/')
    if len(parts) != 3:
        return False

    year, month, day = parts

    if not (year.isdigit() and month.isdigit() and day.isdigit()):
        return False

    year = int(year)
    month = int(month)
    day = int(day)

    if not (1 <= month <= 12):
        return False

    if not (1 <= day <= 31):
        return False

    if month == 2:
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False

    try:
        birthdate = datetime.date(year, month, day)
    except ValueError:
        return False

    age = calculate_age(birthdate)
    if age < 0 or age > 122:
        return False

    return True


def main():
    while True:
        user_input = input("Enter your birthdate (yyyy/mm/dd): ")
        if is_valid_date(user_input):
            year, month, day = map(int, user_input.split('/'))
            birthdate = datetime.date(year, month, day)
            age = calculate_age(birthdate)
            print(f"You are {age} years old!")
            break
        else:
            print("Invalid date!")


if __name__ == "__main__":
    main()
