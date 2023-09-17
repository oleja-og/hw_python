from add_note import *
from del_note import *

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
            pass
        case "read":
            pass
        case "delete":
            del_note()
