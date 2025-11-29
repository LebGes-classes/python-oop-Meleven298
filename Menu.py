class Menu:
    '''Класс Menu.'''

    def __init__(self, main_ekz) -> None:
        '''Инициализация класса Menu.

        Args:
            main_ekz: Экземпляр класса Main, к которому Menu будет обращаться
                               для выполнения действий.
        '''
        
        self.main_ekz = main_ekz

    def display_menu(self) -> None:
        '''Отображение меню.'''

        print("\n----- ГЛАВНОЕ МЕНЮ -----")
        print("1. Создать нового бакалавра")
        print("2. Показать всех бакалавров")
        print("3. Изменить данные бакалавра")
        print("4. Отчислить бакалавра")
        print("5. Перевести бакалавра на следующий курс")
        print("0. Выход из программы")
        print("------------------------")

    def main_program(self) -> None:
        '''Основной цикл интерактивного меню, делегирующий вызовы к Main.'''

        while True:
            self.display_menu()
            choice = input("Выберите действие: ").strip()

            if choice == '1':
                self.main_ekz.create_bachelor_interactive()
            elif choice == '2':
                self.main_ekz.view_all_bachelors()
            elif choice == '3':
                self.main_ekz.change_selected_bachelor()
            elif choice == '4':
                self.main_ekz.expel_bachelor()
            elif choice == '5':
                self.main_ekz.advance_selected_bachelor_course()
            elif choice == '0':
                print("До свидания!")
                break
            else:
                print("Неверный выбор. Пожалуйста, попробуйте снова.")
