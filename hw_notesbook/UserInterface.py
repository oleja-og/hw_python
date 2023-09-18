from add_note import *
from del_note import *
from edit_note import *
from hw_notesbook.validate import valid_file
from read_notes import *
def menu():
    print("""
    Журнал заметок!!!!
    """)
    print("""
        -add 
        -change
        -read
        -delete
    """)
    print("ваше действие :\n")
    choice = input()
    return choice

def user_choice(choice):
    match choice:
        case "add":
            valid_file()
        case "change":
            edit_note()
        case "read":
            read_notes()
        case "delete":
            del_note()
