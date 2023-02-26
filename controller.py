import view, operations

def start():
    print(view.start_view())
    answ = view.answer()
    if answ == "1":
        operations.create_new_note()
        print()
        start()
    elif answ == "2":
        operations.remove_note()
        print()
        start()
    elif answ == "3":
        operations.searching_note()
        print()
        start()
    elif answ == "4":
        operations.add_info_to_note()
        print()
        start()
    elif answ == "5":
        operations.remove_note()
        print()
        start()
    elif answ == "6":
        operations.show_all_notes()
        print()
        start()
    elif answ == "q" or answ == "Q":
        print("Заметки закрыты.")
    else:
        print("Введен неверный символ!")
        print()
        start()       
