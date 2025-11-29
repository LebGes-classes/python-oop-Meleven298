class Bachelor:
    '''Класс для бакалавра.'''

    def __init__(self, last_name: str="", specialization: str="", course: int=0) -> None:
        '''Инициализация/конструктор класса.

        Args:
            last_name: Фамилия.
            specialization: Специализация.
            course: Курс.
        '''

        self.last_name = last_name
        self.specialization = specialization
        self.course = course

    def get_last_name(self) -> str:
        '''Геттер для фамилии.

        Returns:
            last_name: Фамилия.
        '''

        return self.last_name

    def get_specialization(self) -> str:
        '''Геттер для специализации.

        Returns:
            specialization: Специализация.
        '''

        return self.specialization

    def get_course(self) -> int:
        '''Геттер для курса.

        Returns:
            course: Курс.
        '''

        return self.course

    def set_last_name(self, new_last_name: str) -> None:
        '''Сеттер для фамилии.

        Args:
            new_last_name: Новая фамилия
        '''

        self.last_name = new_last_name

    def set_specialization(self, new_specialization: str) -> None:
        '''Сеттер для специализации.

        Args:
            new_specialization: Новая специализация
        '''

        self.specialization = new_specialization

    def set_course(self, new_course: int) -> None:
        '''Сеттер для курса.

        Args:
            new_course: Новый курс
        '''

        self.course = new_course

    def __str__(self) -> str:
        '''Вывод информации о бакалавре.

        Returns:
            Информация
        '''

        return f"Фамилия бакалавра - {self.last_name}. Он(а) учится на программе {self.specialization} на {self.course} курсе"

    def introducing(self, new_specialization: str="Информация скрыта") -> None:
        '''Метод, в котором бакалавр представляется и говорит о своем курсе.'''

        match self.course:
            case 1:
                print(f"{self.last_name}: Привет! Учиться на 1 курсе программы {self.specialization} оказалось тяжелее, чем можно представить. Но я привыкаю!")
            case 2:
                print(f"{self.last_name}: Привет! Я уже вовсю в сфере {self.specialization}. Продолжаю свое обучение на 2 курсе.")
            case 3:
                print(f"{self.last_name}: Привет! Моментами я уже хотел отчислиться с программы {self.specialization} и перезачислиться на {new_specialization}. Но я до сих пор здесь, 3 курс.")
            case 4:
                print(f"{self.last_name}: Привет! Я на 4 курсе специализации {self.specialization}! Пожелай мне удачи в защите диплома!")

    def plus_course(self) -> None:
        '''Метод для перевода на следующий курс.

        Выводит сообщение о переводе или о том, что студент уже на последнем курсе.
        '''
        
        if self.course < 4:
            self.course += 1
            print(f"{self.last_name} успешно переведен на {self.course}-й курс.")
        elif self.course == 4:
            print(f"{self.last_name} уже на последнем курсе. Готов к выпуску!")
        else:
            print(f"Невозможно перевести {self.last_name} на следующий курс (курс {self.course} некорректен).")
