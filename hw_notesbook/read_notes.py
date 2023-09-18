import json




def read_notes():
    with open("file_add.json", "r", encoding='utf-8') as f:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        data = json.load(f)

    for i in data['notes']:
        print(f"заметка № {i['id']}\n {i['header']}")
    read_one_note()


def read_one_note():
    with open("file_add.json", "r", encoding='utf-8') as f:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        data = json.load(f)
    id = int(input("введите № заметки \n"))

    for i in data['notes']:
        if i['id'] == id:
            print(f"{i['body']}\n {i['date']}")
            break



