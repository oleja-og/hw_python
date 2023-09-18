from notesbook import Note
import datetime as dt
import json
import os.path

def add_note():
    c = Note()
    c.id = last_id()
    print("enter title")
    c.header = input()
    print("enter body")
    c.body = input()
    c.date = f"{dt.datetime.now()}"
    file_name = "file_add.json"
    data = json.load(open(file_name))
    new_data = {"id":c.id,"header":c.header,"body":c.body, "date":c.date}
    data['notes'].append(new_data)

    with open("file_add.json", "w",  encoding='utf-8') as f:
        json.dump(data,f,indent=4)

def creat_notesbook():
    data = {}
    data['notes'] = []

    with open("file_add.json", "w",  encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def change_id_note_afterdel():
    file_name = "file_add.json"
    data = json.load(open(file_name))
    id = 1
    for i in data["notes"]:
        i['id'] = id
        id+=1
    with open("file_add.json", "w") as  f:
        json.dump(data,f, indent=4)



def last_id():
    file_name = "file_add.json"
    data = json.load(open(file_name))
    print(data)
    if data['notes'] == []:
        id = 1
        return id
    else:
        id = 1
        for i in data["notes"]:
            if i['id'] == id:
                id += 1
        return id