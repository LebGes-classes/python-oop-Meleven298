class Bachelor:
    def __init__(self, last_name="", specialization="", course=0):
        self.last_name = last_name
        self.specialization = specialization
        self.course = course

    def get_last_name(self) -> str:
        return self.last_name 
    
    def get_specialization(self) -> str:
        return self.specialization
    
    def get_course(self) -> int:
        return self.course
    
    def set_last_name(self, new_last_name):
        self.last_name = new_last_name
    
    def set_specialization(self, new_specialization):
        self.specialization = new_specialization
    
    def set_course(self, new_course):
        self.course = new_course

    def __str__(self) -> str:
        return f"Фамилия бакалавра - {self.last_name}. Он(а) учится на программе {self.specialization} на {self.course} курсе"
    
    def display_info(self):
        print(self) 
    
    def introducing(self, new_specialization) -> str:
        match self.course:
            case 1:
                return f"{self.last_name}: Привет! Учится на 1 курсе программы {self.specialization} оказалось тяжелее, чем можно представить. Но я привыкаю!"
            case 2:
                return f"{self.last_name}: Привет! Я уже вовсю в сфере {self.specialization}. Продолжаю свое обучение на 2 курсе."
            case 3:
                return f"{self.last_name}: Привет! Моментами я уже хотел отчислиться с программы {self.specialization} и перезачислиться на {new_specialization}. Но я до сих пор здесь, 3 курс."
            case 4:
                return f"{self.last_name}: Привет! Я на 4 курсе специализации {self.specialization}! Пожелай мне удачи в защите диплома!"
        
    def plus_course(self):
        if self.course < 4:
            self.course += 1 

            print(f"{self.last_name} успешно переведен на {self.course}-й курс.")
        elif self.course == 4:
            print(f"{self.last_name} уже на последнем курсе. Готов к выпуску!")
        else:
            print(f"Невозможно перевести {self.last_name} на следующий курс (ошибка данных).")

all_bachelors = []

class Main:
    def demonstration(self):
        print("\n---Здравствуйте! Позвольте продемонстрировать создание двух обьектов класса бакалавр с параметрами и без---")

        try:
            Marsel = Bachelor("Валеев", "Аналитика", 1)
            all_bachelors.append(Marsel)
            print(f"1. Создан экземпляр (с параметрами): {Marsel}")

            Anton = Bachelor()
            all_bachelors.append(Anton)
            print(f"2. Создан экземпляр (без параметров): {Anton}")

            print("\n   -> Демонстрация изменения полей через сеттеры:")
            Anton.last_name = "Петров"
            Anton.specialization = "Физика"
            Anton.course = 3
            print(f"   Изменен экземпляр 2 через сеттеры: {Anton}")
            print("Также они могут рассказать немного о своей учебе:")
            print(Marsel.introducing(Anton.get_specialization()))
            print(Anton.introducing(Marsel.get_specialization()))
            print("")
            print("И быть отчисленными.")
        except Exception as e:
            print(f"Ошибка при демонстрации: {e}")

        print("\n--- Конец демонстрации ---\n")
        Menu.main_program(self)

    def create_bachelor_interactive(self):
        try:
            last_name_interactive = input("Введите фамилию студента:")
            specialization_interactive = input("Введите специальность студента:")
            course_interactive = int(input("Введите курс студента:"))

            created_bachelor = Bachelor(last_name_interactive, specialization_interactive, course_interactive)
            all_bachelors.append(created_bachelor)

            print("Бакалавр создан")

            created_bachelor.display_info(self)
        except ValueError as e:
            print(f"Ошибка при создании бакалавра: {e}")
        except Exception as e:
            print(f"Неожиданная ошибка: {e}")


    def view_all_bachelors(self):
        print("-----Список всех бакалавров-----")

        if not all_bachelors:
            return False
        for i, bachelor in enumerate(all_bachelors):
            print(f"{i+1}. {bachelor}")

        return True


    def select_bachelor(self):
        if not self.view_all_bachelors():
            return None
        while True:
            try:
                choice = input("Введите номер бакалавра для выбора (или 0 для отмены): ").strip()
                if choice == '0':
                    print("Выбор отменен.")
                    return None
                
                index = int(choice) - 1
                if 0 <= index < len(all_bachelors):
                    return all_bachelors[index]
                else:
                    print("Неверный номер. Пожалуйста, попробуйте снова.")
            except ValueError:
                print("Неверный ввод. Пожалуйста, введите число.")


    def expel_bachelor(self):
        expeling_bachelor = self.select_bachelor()
        
        if not expeling_bachelor:
            return

        for bachelor in all_bachelors:
            if bachelor == expeling_bachelor:
                all_bachelors.remove(bachelor)

        print(f"{expeling_bachelor.last_name} отчислен")
        print(all_bachelors)


    def change_selected_bachelor(self):
        print("--- Изменение данных бакалавра ---")
        changing_bachelor = self.select_bachelor()
        if not changing_bachelor:
            return

        print(f"Выбран: {changing_bachelor}")
        print("Что вы хотите изменить?")
        print("1. Фамилия")
        print("2. Специальность")
        print("3. Курс")
        print("4. Cпросить как дела")
        print("5. Отчислить")
        print("6. Отменить")

        while True:
            choice = input("Введите ваш выбор: ").strip()
            if choice == '1':
                try:
                    new_last_name = input("Введите новую фамилию: ")
                    changing_bachelor.last_name = new_last_name

                    print("Фамилия успешно изменена.")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                break
            elif choice == '2':
                try:
                    new_specialization = input("Введите новую специализацию: ")
                    changing_bachelor.specialization = new_specialization

                    print("Специализация успешно изменена")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                break
            elif choice == '3':
                try:
                    new_course = input("Введите новый курс: ")
                    changing_bachelor.course = new_course

                    print("Курс успешно изменен")
                except ValueError as e:
                    print(f"Ошибка: {e}")
                break
            elif choice == '4':
                print(changing_bachelor.introducing("Авиастроение"))
            elif choice == '5':
                self.expel_bachelor()
            elif choice == '6':
                print("Изменение отменено.")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
        print(f"Новые данные: {changing_bachelor}")

class Menu:
    def main_program(self):
        while True:
            print("\n--- Главное меню ---")
            print("1. Создать нового бакалавра")
            print("2. Просмотреть всех бакалавров")
            print("3. Изменить данные бакалавра")
            print("4. Перевести бакалавра на следующий курс")
            print("5. Завершить работу")

            choice = input("Введите ваш выбор: ").strip()

            match choice:
                case '1':
                    self.create_bachelor_interactive()
                case '2':
                    self.view_all_bachelors()
                case '3':
                    self.change_selected_bachelor()
                case '4':
                    smart_bachelor = self.select_bachelor()
                    smart_bachelor.plus_course()
                case '5':
                    print("Завершение работы программы. До свидания!")

                    return False
                case _:
                    print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    Main.demonstration(Main())