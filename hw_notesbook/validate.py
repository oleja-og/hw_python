import json
import os.path

from hw_notesbook.add_note import add_note, creat_notesbook


def valid_file():
    if  os.path.exists("file_add.json") == True:
        add_note()
    else:
        creat_notesbook()
        add_note()

