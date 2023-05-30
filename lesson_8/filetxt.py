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

def delete_contact():
    with open('file.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        print("введите имя для удаления: ")
        name = input("фио : ")
        for i in data:
            if name not in i:
                with open('file1.txt', 'a') as file1:
                    file1.write(i)
    with open("file.txt", "w") as file:
        file.close()
    with open('file1.txt', 'r', encoding="utf8") as file1:
        data = file1.readlines()
        for i in data:
            with open("file.txt", "a") as file:
                file.write(i)
    with open('file1.txt', 'w', encoding="utf8") as file1:
        file1.close()


def rename_contact():
    with open('file.txt', 'r', encoding="utf8") as file:
        data = file.readlines()
        print("введите имя для изменения: ")
        name = input("фио : ")
        for i in data:
            if name in i:
                print("+")
                print("введите другое имя: ")
                rename = input("фио : ")
                with open('file1.txt', 'a') as file1:
                    file1.write(i.replace(name, rename))
            else:
                with open('file1.txt', 'a') as file1:
                    file1.write(i)
    with open("file.txt", "w") as file:
        file.close()
    with open('file1.txt', 'r', encoding="utf8") as file1:
        data = file1.readlines()
        for i in data:
            with open("file.txt", "a") as file:
                file.write(i)
    with open('file1.txt', 'w', encoding="utf8") as file1:
        file1.close()