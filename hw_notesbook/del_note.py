import json
from add_note import change_id_note_afterdel
def del_note():
    header = str(input("Ввведите заголовок заметки для удаления\n"))
    with open("file_add.json", "r", encoding='utf-8') as f:
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        data = json.load(f)
    count = 0
    for i in data['notes']:
        if i["header"] == header:
            data["notes"].pop(count)
        else:
            count+=1

    with open("file_add.json", "w") as  f:
        json.dump(data,f, indent=4)
    change_id_note_afterdel()


