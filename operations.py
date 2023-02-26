import view, operations, controller
import os

all_notes = []

def create_new_note():
    file_name = view.f_name()
    if os.path.isfile(file_name):
        print("Заметка с таким именем существует!")
        create_new_note()
    elif (file_name.replace(".txt", "")) == "q" or (file_name.replace(".txt", "")) == "Q":
        print("Данное имя недопустимо!")
        create_new_note()   
    else:
        with open (file_name, 'w', encoding='utf-8') as file:
            file.write(view.note_text())
        all_notes.append(file_name.replace(".txt", ""))

def searching_note():
    operations.good_view()
    file_name = view.f_name()
    if (file_name.replace(".txt", "")) == "q" or (file_name.replace(".txt", "")) == "Q":
        controller.start()
    elif os.path.isfile(file_name):
        with open (file_name, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    else:
        print("Такой заметки не существует!")
        print("Введите q, если хотите выйти в основное меню")
        searching_note()

def add_info_to_note():
    operations.good_view()
    file_name = view.f_name()
    if (file_name.replace(".txt", "")) == "q" or (file_name.replace(".txt", "")) == "Q":
        controller.start()
    elif os.path.isfile(file_name):
        with open (file_name, 'a', encoding='utf-8') as file:
            file.write(view.note_text())
        print("Добавлено!")
    else:
        print("Такой заметки не существует!")
        print("Введите q, если хотите выйти в основное меню")
        add_info_to_note()

def show_all_notes():
    [print (i) for i in all_notes]

def remove_note():
    operations.good_view()
    file_name = view.f_name()
    if (file_name.replace(".txt", "")) == "q" or (file_name.replace(".txt", "")) == "Q":
        controller.start()
    elif os.path.isfile(file_name):
        all_notes.remove(file_name.replace(".txt", ""))
        os.remove(file_name)
        print("Удалено!")
    else: 
        print("Такой заметки не существует!")
        print("Введите q, если хотите выйти в основное меню")
        remove_note()