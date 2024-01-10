from note_manager import NoteManager

"""Задание 1. Приложение учёта животных в питомнике (Python)
В программе должен быть реализован следующий функционал:
14.1 Завести новое животное
14.2 определять животное в правильный класс
14.3 увидеть список команд, которое выполняет животное
14.4 обучить животное новым командам
14.5 Реализовать навигацию по меню
"""


def choose_type():
    print('''Выберете катеогрию добавляемого животного:
    1 - Собака
    2 - Кошка
    3 - Хомяк
    4 - Лошадь
    5 - Верблюд
    6 - Осёл
    7 - Вернуться в основное меню
    8 - Выход из проргаммы
    ''')

    pet_type = input()

    match pet_type:
        case '1':
            print('добавляем собаку')
            return 'Собака'
        case '2':
            print('добавляем кошку')
            return 'Кошка'
        case '3':
            print('добавляем хомяка')
            return 'Хомяк'
        case '4':
            print('добавляем лошадь')
            return 'Лошадь'
        case '5':
            print('добавляем верблюда')
            return 'Верблюд'
        case '6':
            print('добавляем осла')
            return 'Осёл'
        case '7':
            print('выход в основное меню')
            return '7'
        case '8':
            print('выход из программы')
            return -1
        case _:
            print("Неверное значение")
            return '7'




def get_pet_class(name):
    if name in ('Собака', 'Кошка', 'Хомяк'):
        return 'Домашние животные'
    elif name in ('Лошадь', 'Верблюд', 'Осёл'):
        return 'Вьючные животные'
    else:
        return 'Класс не определён'


def main():
    note_manager = NoteManager("base_animal.json")

    while True:
        print("Доступные команды:")
        print("1. Создать животное")
        print("2. Просмотреть животных с фильтрацией по дате")
        print("3. Добавить команды животному")
        print("4. Удалить животное")
        print("5. Просмотреть животное по ID")
        print("6. Просмотреть команды животного по ID")
        print("7. Просмотреть всех животных")
        print("8. Выйти из программы.\n")

        choice = input("Введите номер команды: ")

        if choice == "1":

            pet_type = choose_type()
            if pet_type == '7':
                main()
                break
            elif pet_type == -1:
                break

            pet_class = get_pet_class(pet_type)
            name_pet = input("Введите кличку животного: ")
            commands = input("Введите команды для животного: ")
            note_manager.create_note(name_pet, commands, pet_type, pet_class)
            print("Животное успешно добавлено!\n")

        elif choice == "2":
            try:
                date_filter = input("Введите дату фильтрации (гггг-мм-дд): ")
                note_manager.read_notes(date_filter)
            except ValueError:
                print("Неверный ввод")
                main()
                break

        elif choice == "3":
            try:
                note_id = int(
                    input("Введите ID животного, у которого хотите добавить команд: "))
                new_commands = input("Введите через запятую команды для животного: ")
                note_manager.edit_note(note_id, new_commands)
                print("Команды успешно обновлены!\n")
            except ValueError:
                print("Неверный ID")
                main()
                break


        elif choice == "4":
            note_id = int(
                input("Введите ID животного, которое хотите удалить: "))
            note_manager.delete_note(note_id)
            print("Такой записи больше нет!\n")

        elif choice == "5":
            try:
                note_id = int(input("Введите ID животного для просмотра:"))
                note_manager.view_note(note_id)
                print("\n")
            except ValueError:
                print("Ошибка ввода")
                main()
                break

        elif choice == "6":
            try:
                note_id = int(input("Введите ID животного для просмотра команд:"))
                note_manager.view_note_commands(note_id)
                print("\n")
            except ValueError:
                print("Ошибка ввода")
                main()
                break

        elif choice == "7":
            print("Список всех животных:\n")
            note_manager.view_all_notes()
            print("\n")

        elif choice == "8":
            print("Программа завершена.")
            print("\n")
            break

        else:
            print("Неверная команда. Попробуйте снова.\n")


if __name__ == "__main__":
    main()
