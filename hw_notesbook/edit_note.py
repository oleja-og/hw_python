import json
import datetime as dt
from add_note import change_id_note_afterdel

def edit_note():
    id = int(input("Ввведите id заметки для редактирования\n"))
    with open("file_add.json", "r", encoding='utf-8') as f:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        data = json.load(f)
    for i in data['notes']:
        if i["id"] == id:
            print("enter title")
            i["header"] = input()
            print("enter body")
            i['body'] = input()
            i['date'] = f"{dt.datetime.now()}"
        else:
            print("такого id нет в списке")

    with open("file_add.json", "w") as f:
        json.dump(data, f, indent=4)