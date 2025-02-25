# TODO: описать базовый класс
class Animal:
    """
    Базовый класс для животных.
    """

    def __init__(self, name: str, age: int) -> None:
        """
        Конструктор класса Animal.
        :param name: Имя животного.
        :param age: Возраст животного.
        """
        self._name = name  # Инкапсуляция: имя доступно только внутри класса
        self._age = age    # Инкапсуляция: возраст доступен только внутри класса

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Animal.
        """
        return f"Имя животного - {self._name}, возраст животного - {self._age}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Animal для разработчиков.
        """
        return f"Animal(name='{self._name}', age={self._age})"

    def make_sound(self) -> str:
        """
        Возвращает звук, издаваемый животным.
        """
        return "Animal sound"

# TODO: описать дочерний класс
class Cat(Animal):
    """
    Дочерний класс для кошек.
    """

    def __init__(self, name: str, age: int, breed: str) -> None:
        """
        Конструктор класса Cat.
        :param name: Имя кошки.
        :param age: Возраст кошки.
        :param breed: Порода кошки.
        """
        super().__init__(name, age)  # Вызов конструктора родительского класса
        self.breed = breed

    def __str__(self) -> str:
        """
        Возвращает строковое представление объекта Cat.
        """
        return f"Имя кошки - {self._name}, возраст - {self._age}, порода - {self.breed}"

    def __repr__(self) -> str:
        """
        Возвращает строковое представление объекта Cat для разработчиков.
        """
        return f"Cat(name='{self._name}', age={self._age}, breed='{self.breed}')"

    def make_sound(self) -> str:
        """
        Возвращает звук, издаваемый кошкой. Перегрузка метода make_sound из базового класса.
        Перегрузка необходима, так как кошки издают звук, отличающийся от общего звука животных.
        """
        return "Meow!"

    def play(self, item: str) -> str:
        """
        Кошка играет с предметом.
        :param item: Предмет, с которым кошка играет.
        Возвращает сообщение о том, что кошка играет с предметом.
        """
        return f"Cat {self._name} playing with {item}."

animal = Animal("Aaaa", 7)
print(animal)  # Вывод: Имя животного - Aaaa, возраст животного - 7
print(repr(animal)) # Вывод: Animal(name='Aaaa', age=7)
print(animal.make_sound()) # Вывод: Animal sound

cat = Cat("Musa", 3, "Britain")
print(cat)  # Вывод: Имя кошки - Musa, возраст - 3, порода - Britain
print(repr(cat)) # Вывод: Cat(name='Musa', age=3, breed='Britain')
print(cat.make_sound())  # Вывод: Meow!
print(cat.play("ball"))  # Вывод: Cat Musa playing with ball.