import operations

def note_name():
    return input("Введите название заметки: ")

def note_text():
    return input("Введите текст заметки: ")

def f_name():
    name = note_name()
    file_name = name + '.txt'
    return file_name

def good_view():
    print()
    operations.show_all_notes()
    print()

def start_view():
    return ("Выберите действие и введите номер, либо 'q', чтобы выйти:\n"
            "1. Создать заметку\n"
            "2. Удалить заметку\n"
            "3. Найти и показать заметку\n"
            "4. Добавить информацию в заметку\n"
            "5. Удалить заметку\n"
            "6. Показать список заметок")

def answer():
    return input("Ответ: ")