if __name__ == "__main__":
    # Write your solution here
    pass
class Animal:
    """
    Базовый класс для всех животных.
    Атрибуты:
    - name (str): Имя животного.
    - age (int): Возраст животного.
    - species (str): Вид животного.
    """

    def __init__(self, name: str, age: int, species: str) -> None:
        """
        Конструктор класса Animal.
        :param name: Имя животного.
        :param age: Возраст животного.
        :param species: Вид животного.
        """
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self) -> str:
        """
        Метод для издания звука животным.
        :return: Строка с описанием звука.
        """
        return f"{self.name} издает звук."

    def __str__(self) -> str:
        """
        Магический метод для строкового представления объекта.
        :return: Строка с описанием животного.
        """
        return f"{self.species} по имени {self.name}, возраст {self.age} лет."

    def __repr__(self) -> str:
        """
        Магический метод для представления объекта в виде строки, пригодной для воссоздания объекта.
        :return: Строка с описанием объекта.
        """
        return f"Animal(name={self.name!r}, age={self.age!r}, species={self.species!r})"

    class Dog("Animal"):
        """
        Дочерний класс для собак.
        Атрибуты:
        - breed (str): Порода собаки.
        - is_trained (bool): Признак дрессированности собаки.
        """

        def __init__(self, name: str, age: int, breed: str, is_trained: bool = False) -> None:
            """
            Конструктор класса Dog.
            :param name: Имя собаки.
            :param age: Возраст собаки.
            :param breed: Порода собаки.
            :param is_trained: Признак дрессированности собаки.
            """
            super().__init__(name, age, species="Собака")
            self.breed = breed
            self.is_trained = is_trained

        def make_sound(self) -> str:
            """
            Перегрузка метода make_sound для собаки.
            :return: Строка с описанием звука собаки.
            """
            return f"{self.name} лает: Гав-гав!"

        def fetch(self, item: str) -> str:
            """
            Метод для выполнения команды "принеси".
            :param item: Предмет, который нужно принести.
            :return: Строка с описанием действия.
            """
            return f"{self.name} приносит {item}."

        def __str__(self) -> str:
            """
            Перегрузка магического метода для строкового представления объекта.
            :return: Строка с описанием собаки.
            """
            return f"{self.species} породы {self.breed} по имени {self.name}, возраст {self.age} лет."

        def __repr__(self) -> str:
            """
            Перегрузка магического метода для представления объекта в виде строки, пригодной для воссоздания объекта.
            :return: Строка с описанием объекта.
            """
            return f"Dog(name={self.name!r}, age={self.age!r}, breed={self.breed!r}, is_trained={self.is_trained!r})"

        class Cat("Animal"):
            """
            Дочерний класс для кошек.
            Атрибуты:
            - color (str): Цвет кошки.
            - is_indoor (bool): Признак домашней кошки.
            """

            def __init__(self, name: str, age: int, color: str, is_indoor: bool = True) -> None:
                """
                Конструктор класса Cat.
                :param name: Имя кошки.
                :param age: Возраст кошки.
                :param color: Цвет кошки.
                :param is_indoor: Признак домашней кошки.
                """
                super().__init__(name, age, species="Кошка")
                self.color = color
                self.is_indoor = is_indoor

            def make_sound(self) -> str:
                """
                Перегрузка метода make_sound для кошки.
                :return: Строка с описанием звука кошки.
                """
                return f"{self.name} мяукает: Мяу-мяу!"

            def purr(self) -> str:
                """
                Метод для описания мурлыканья кошки.
                :return: Строка с описанием действия.
                """
                return f"{self.name} мурлычет."

            def __str__(self) -> str:
                """
                Перегрузка магического метода для строкового представления объекта.
                :return: Строка с описанием кошки.
                """
                return f"{self.species} цвета {self.color} по имени {self.name}, возраст {self.age} лет."

            def __repr__(self) -> str:
                """
                Перегрузка магического метода для представления объекта в виде строки, пригодной для воссоздания объекта.
                :return: Строка с описанием объекта.
                """
                return f"Cat(name={self.name!r}, age={self.age!r}, color={self.color!r}, is_indoor={self.is_indoor!r})"

            # Создание объектов
            animal = "Animal"("Бобик", 5, "Собака")
            dog = "Dog"("Рекс", 3, "Овчарка", True)
            cat = "Cat"("Мурка", 2, "Серая", True)

            # Вывод информации о животных
            print(animal)  # Собака по имени Бобик, возраст 5 лет.
            print(dog)  # Собака породы Овчарка по имени Рекс, возраст 3 лет.
            print(cat)  # Кошка цвета Серая по имени Мурка, возраст 2 лет.

            # Вызов методов
            print(animal.make_sound())  # Бобик издает звук.
            print(dog.make_sound())  # Рекс лает: Гав-гав!
            print(cat.make_sound())  # Мурка мяукает: Мяу-мяу!

            print(dog.fetch("мяч"))  # Рекс приносит мяч.
            print(cat.purr())  # Мурка мурлычет.