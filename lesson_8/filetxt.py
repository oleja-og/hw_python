def enter_family():
    name = input("ФИО :").lower()
    number = input("номер :")

    with open("file.txt", "a", encoding="utf8") as file:
        file.write(f"{name} тел. {number}\n")


def output_all():
    with open('file.txt', 'r', encoding="utf8" ) as file:
        data = file.readlines()
        for i in data:
            print(i)


def search_family():
    with open('file.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        print("введите имя для поиска: ")
        name = input("фио : ")
        for i in data:
            if name in i:
                print(i)
                break
