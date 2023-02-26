import view
import os

def create_new_note():
    name = view.note_name()
    file_name = name + '.txt'
    if os.path.isfile(file_name):
        print("Заметка с таким именем существует!")
        create_new_note()
    else:
        with open (file_name, 'w', encoding='utf-8') as file:
            file.write(view.note_text())
        with open ("all_notes.txt", 'a', encoding='utf-8') as file:
            file.write(name + "\n")

def searching_note():
    name = view.note_name()
    file_name = name + ".txt"
    if os.path.isfile(file_name):
        with open (file_name, 'r', encoding='utf-8') as file:
            for line in file:
                print(line.strip())
    else:
        print("Такой заметки не существует!")
        searching_note()

