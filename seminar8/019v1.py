def read_csv(filename: str) -> list:
    data = []
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    with open(filename, "r", encoding="utf-8") as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(",")))
            data.append(record)
        return data


def show_record(record: dict):
    print("#"*10)
    for key in record:
        print(f"{key} : {record[key]}")
    print("#"*10)            


def show_phonebook(phone_book: list):
    for elem in phone_book:
        show_record(elem)
        print()


def find_by_name(phone_book: list, name: str):
    results = []
    for elem in phone_book:
        if elem ["Фамилия"] == name:
            results.append(elem)
    return results        
def find_by_number(phone_book: list, number: str):
    results = []
    for elem in phone_book:
        if elem ["Телефон"] == number:
            results.append(elem)
    return results         

def get_file_name():
    return input("Введите имя файла для сохранения: ")

def write_csv(filename: str, data: list):
    with open(filename, "w", encoding="utf-8") as fout:
        for i in range(len(data)):
            s = ""
            for v in data[i].values():
                s += v + ","
                fout.write(f"{s[:-1]}\n")

def write_txt(filename: str, data: list):
    with open(filename, "w", encoding="utf-8") as fout:
        for i in range(len(data)):
            s = ""
            for v in data[i].values():
                s += v + ","
                fout.write(f"{s[:-1]}\n")



def get_search_name():
    return input("Введите фамилию для поиска: ")

def show_menu() -> int:
    print("\nВыберите необходимое действие:\n"
             "1. Отобразить весь справочник\n"
             "2. Найти абонента по фамилии\n"
             "3. Найти абонента по номеру телефона\n"
             "4. Добавить абонента в справочник\n"
             "5. Сохранить справочник в текстовом формате\n"
             "6. Закончить работу")
    choice =int(input())
    return choice

def get_search_number():
    return input("Введите номер телефона для поиска: ")

def get_new_user():
    record = dict()
    fields = ["Фамилия", "Имя", "Телефон", "Описание"]
    for field in fields:
        record[field] = input(f"Введите {field}")
    return record

def add_user(phone_book:list,record:dict):
    phone_book.append(record)    

def work_with_phonebook():
    choice = show_menu()
    phone_book = read_csv("phonebook.csv")

    while (choice != 6):
        if choice == 1:
            show_phonebook(phone_book)
        elif choice == 2:
            name = get_search_name()
            show_phonebook(find_by_name(phone_book, name))
        elif choice == 3:
            number = get_search_number()
            print(find_by_number(phone_book, number))
        elif choice == 4:
            user_data = get_new_user()
            add_user(phone_book, user_data)
            write_csv("phonebook.csv", phone_book)
        elif choice == 5:
            file_name = get_file_name()
            write_csv(file_name, phone_book)
        choice = show_menu()          


if __name__ == "___main___":
    work_with_phonebook()                  
                 