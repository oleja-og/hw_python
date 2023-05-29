from interface import *
from filetxt import *

while True:
    interface()
    choice = int(input("Ваше действие: "))
    if choice == 1:
        add_family()
        enter_family()
    elif choice == 2:
        list_contacts()
        output_all()
        print("нажмите ентер чтобы продолжить....")
        input()
    elif choice == 3:
        search_contact()
        search_family()
        print("нажмите ентер чтобы продолжить....")
        input()
    elif choice == 4:
        exit()
        break
    else:
        print("Неправильное действие введите цифру от 1 до 4 !!!")
        print("нажмите ентер чтобы продолжить....")
        input()
