def capitalize_name(name):
    string = ' '
    for part in name.split():
        part = part.capitalize()
        string = string + part
    return string


# def read_people_data(file_path):
#     people = []
#     file = open(file_path, 'r', encoding='utf-8')
#     headers = file.readline().strip().split(',')
#     for line in file:
#         values = line.strip().split(',')
#         person = dict(zip(headers, values))
#         person['email'] = person['email'].lower()
#         people.append(person)
#     file.close()
#     return people
def read_people_data(file_path):
    people = []
    file = open(file_path, 'r', encoding='utf-8')
    headers = file.readline().strip().split(',')
    for line in file:
        values = line.strip().split(',')
        person = {headers[i]: values[i] for i in range(len(headers))}  # 使用字典推导来创建字典
        person['email'] = person['email'].lower()
        people.append(person)

    return people


def main():
    file_path = 'data/people.csv'
    people = read_people_data(file_path)

    name_to_search = input("Enter a name: ").strip().lower()

    person_found = None
    for person in people:
        if person['name'].strip().lower() == name_to_search:
            person_found = person
            break

    if person_found:
        print(f"Name: {capitalize_name(person_found['name'])}")
        print(f"Country: {capitalize_name(person_found['country'])}")
        print(f"Email: {person_found['email']}")
    else:
        print("Name not found!")


if __name__ == "__main__":
    main()
