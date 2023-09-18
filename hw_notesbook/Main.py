from UserInterface import menu
from hw_notesbook.del_note import del_note
from hw_notesbook.edit_note import edit_note
from hw_notesbook.read_notes import read_notes
from hw_notesbook.validate import valid_file

key = True
while key:
    choice = menu()
    match choice:
        case "add":
            valid_file()
        case "change":
            edit_note()
        case "read":
            read_notes()
        case "delete":
            del_note()
        case "exit":
            print("Вы вышли из журнала заметок")
            key = False


