from Bachelor import Bachelor
from Menu import Menu

class Main:
    '''Класс для Main.'''

    def __init__(self) -> None:
        '''Инициализация класса Main.
        Создает пустой список для хранения бакалавров.'''

        self.all_bachelors: list[Bachelor] = []

    def demonstration(self) -> None:
        '''Демонстрация создания двух объектов класса бакалавр с параметрами и без.'''

        print("\n---Здравствуйте! Позвольте продемонстрировать создание двух обьектов класса бакалавр с параметрами и без---")

        try:
            marsel = Bachelor("Валеев", "Аналитика", 1)
            self.all_bachelors.append(marsel)

            print(f"1. Создан экземпляр (с параметрами): {marsel}")

            anton = Bachelor()
            self.all_bachelors.append(anton)

            print(f"2. Создан экземпляр (без параметров): {anton}")
            print("\n   -> Демонстрация изменения полей через сеттеры:")

            anton.set_last_name("Петров")
            anton.set_specialization("Физика")
            anton.set_course(3)

            print(f"   Изменен экземпляр 2 через сеттеры: {anton}")
            print("Также они могут рассказать немного о своей учебе:")

            marsel.introducing(anton.get_specialization())
            anton.introducing(marsel.get_specialization())
            print("")
            print("И быть отчисленными.")

        except Exception as e:
            print(f"Ошибка при демонстрации: {e}")

        print("\n--- Конец демонстрации ---\n")

        menu_instance = Menu(self)
        menu_instance.main_program()

    def create_bachelor_interactive(self) -> None:
        '''Создает бакалавра интерактивным образом, запрашивая данные у пользователя.'''

        try:
            last_name_interactive = input("Введите фамилию студента: ")
            specialization_interactive = input("Введите специальность студента: ")
            course_interactive = int(input("Введите курс студента (1-4): "))

            created_bachelor = Bachelor(last_name_interactive, specialization_interactive, course_interactive)
            self.all_bachelors.append(created_bachelor)

            print("\n Бакалавр успешно создан!")
            print(created_bachelor)
            
        except ValueError as e:
            print(f"Ошибка при создании бакалавра: {e}")
        except Exception as e:
            print(f"Произошла неожиданная ошибка: {e}")

    def view_all_bachelors(self) -> bool:
        '''Показывает список всех бакалавров.

        Returns:
            True, если список не пуст, иначе False.
        '''

        print("\n----- Список всех бакалавров -----")

        if not self.all_bachelors:
            print("Список бакалавров пуст.")
            return False
        for i, bachelor in enumerate(self.all_bachelors):
            print(f"{i+1}. {bachelor}")

        print("---------------------------------")

        return True

    def select_bachelor(self) -> Bachelor | None:
        '''Позволяет пользователю выбрать бакалавра из списка.

        Returns:
            Выбранный объект Bachelor или None, если выбор отменен или список пуст.
        '''

        if not self.view_all_bachelors():
            return None
        while True:
            try:
                choice = input("Введите номер бакалавра для выбора (или 0 для отмены): ").strip()
                if choice == '0':
                    print("Выбор отменен.")
                    return None
                index = int(choice) - 1
                if 0 <= index < len(self.all_bachelors):
                    return self.all_bachelors[index]
                else:
                    print("Неверный номер. Пожалуйста, попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")

    def expel_bachelor(self) -> None:
        '''Исключает выбранного бакалавра из списка.'''

        print("\n--- Отчисление бакалавра ---")

        expelling_bachelor = self.select_bachelor()
        if not expelling_bachelor:
            return

        try:
            self.all_bachelors.remove(expelling_bachelor)
            print(f"{expelling_bachelor.last_name} успешно отчислен.")
            self.view_all_bachelors()
        except ValueError:
            print("Ошибка: Выбранный бакалавр не найден в списке.")
        except Exception as e:
            print(f"Произошла неожиданная ошибка при отчислении: {e}")

    def change_selected_bachelor(self) -> None:
        '''Позволяет изменить данные выбранного бакалавра.'''

        print("\n--- Изменение данных бакалавра ---")

        changing_bachelor = self.select_bachelor()
        if not changing_bachelor:
            return

        print(f"Выбран: {changing_bachelor}")
        print("Что вы хотите изменить?")
        print("1. Фамилия")
        print("2. Специальность")
        print("3. Курс")
        print("4. Попросить представиться (рассказать о себе)")
        print("0. Отменить")

        while True:
            choice = input("Введите ваш выбор: ").strip()

            if choice == '1':
                new_last_name = input("Введите новую фамилию: ")
                changing_bachelor.set_last_name(new_last_name)
                print("Фамилия успешно изменена.")
                break
            elif choice == '2':
                new_specialization = input("Введите новую специализацию: ")
                changing_bachelor.set_specialization(new_specialization)
                print("Специализация успешно изменена.")
                break
            elif choice == '3':
                try:
                    new_course = int(input("Введите новый курс (1-4): "))
                    changing_bachelor.set_course(new_course)
                    print("Курс успешно изменен.")
                except ValueError as e:
                    print(f"Ошибка при изменении курса: {e}")
                break
            elif choice == '4':
                changing_bachelor.introducing()
                break
            elif choice == '0':
                print("Изменение отменено.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")

    def advance_selected_bachelor_course(self) -> None:
        '''Метод для перевода выбранного бакалавра на следующий курс.'''

        print("\n--- Перевод бакалавра на следующий курс ---")

        selected_bachelor = self.select_bachelor()
        if not selected_bachelor:
            return
        selected_bachelor.plus_course()


if __name__ == "__main__":
    main = Main()
    main.demonstration()

