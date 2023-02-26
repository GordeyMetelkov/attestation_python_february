def note_name():
    return input("Введите название заметки: ")
def note_text():
    return input("Введите текст заметки: ")
def f_name():
    name = note_name()
    file_name = name + '.txt'
    return file_name