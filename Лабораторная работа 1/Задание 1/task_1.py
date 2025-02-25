# TODO: Подробно описать три произвольных класса
import doctest
from typing import List, Tuple


# TODO: описать класс
class Car:
    def __init__(self, speed: int, power: int):
        """
        Создание и подготовка к работе объекта "Машина"

        :param speed: Скорость машины.
        :param power: Количество лошадиных сил машины.

        :raise ValueError: Если количество лошадиных сил не попадает
         в заданный диапазон, то возвращается ошибка.
        :raise ValueError: Если скорость не попадает
         в заданный диапазон, то возвращается ошибка.

        Примеры:
        >>> car = Car(speed=60, power=1000)  # инициализация машины
        """
        if not (0 <= power <= 2000):
            raise ValueError("Количество лошадиных сил машины должно быть в диапазоне от 0 до 2000.")
        if not (0 <= speed <= 200):
            raise ValueError("Скорость должна быть в диапазоне от 0 до 200 км/ч.")

        self.speed: int = speed
        self.power: int = power
        self.contents: List[Tuple[str, int]] = []

    def add_item(self, item: str, quantity: int) -> str:
        """
        Функция, которая добавляет предметы в машину.

        :param item: Предмет, добавляемый в машину.
        :param quantity: Количество предмета.

        :return: Сколько единиц предмета добавлено в машину.
        :raise ValueError: Если количество предметов задано
         отрицательным, то возвращается ошибка.
        """
        if quantity <= 0:
            raise ValueError("Количество должно быть положительным.")
        self.contents.append((item, quantity))
        return f"Добавлено {quantity} единиц {item}."

    def adjust_speed(self, new_speed: int) -> str:
        """
        Функция, которая изменяет скорость машины.
        :param new_speed: Новая заданная скорость.

        :return: Какая скорость установлена для машины.
        :raise ValueError: Если заданная скорость не попадает в необходимый диапазон,
        то возвращается ошибка.
        """
        if not (0 <= new_speed <= 200):
            raise ValueError("Новая скорость должна быть в диапазоне от 0 до 200 км/ч.")
        self.speed = new_speed
        return f"Скорость изменена на {new_speed} км/ч."


# TODO: описать ещё класс
class Laptop:
    def __init__(self, brand: str, battery_capacity: int):
        """
        Создание и подготовка к работе объекта "Ноутбук"

        :param brand: Модель ноутбука.
        :param battery_capacity: Емкость батареи.

        :raise ValueError: Если заданная ёмкость батареи не попадает в необходимый диапазон,
         то возвращается ошибка.

        Примеры:
        >>> laptop = Laptop(brand="Redmi", battery_capacity=5100) # инициализация ноутбука
        """
        if battery_capacity <= 0 or battery_capacity > 10000:
            raise ValueError("Ёмкость батареи должна быть от 1 до 10000 мАч.")

        self.brand: str = brand
        self.battery_capacity: int = battery_capacity
        self.battery_level: int = 100

    def gaming(self, duration: int) -> str:
        """
        Функция, которая запускает игры, уменьшая емкость батареи.
        :param duration: Длительность игры.

        :return: Длительность игры и остаток заряда батареи
        :raise ValueError: Если длительность игры задана отрицательной, то возвращается ошибка.
        :raise ValueError: Если количество заряда недостаточно для игры, то возвращается ошибка.
        """
        if duration <= 0:
            raise ValueError("Длительность игры должна быть положительным числом.")
        battery_usage = duration * 2
        if battery_usage > self.battery_level:
            raise ValueError("Недостаточно заряда для игры.")
        self.battery_level -= battery_usage
        return f"Игра длительностью {duration} минут завершена. Остаток заряда: {self.battery_level}%."

    def charge(self, amount: int = 20) -> str:
        """
        Функция, которая заряжает ноутбук.
        :param amount: Количество добавляемого заряда.

        :return: Текущий уровень заряда батареи
        :raise ValueError: Если количество заряда задано отрицательным, то возвращается ошибка.
        """
        if amount <= 0:
            raise ValueError("Количество заряда должно быть положительным.")
        self.battery_level = min(100, self.battery_level + amount)
        return f"Ноутбук заряжен. Текущий уровень заряда: {self.battery_level}%."


# TODO: и ещё один
class Kettle:
    def __init__(self, volume: float, is_on: bool = False):
        """
        Создание и подготовка к работе объекта "Чайник"

        :param volume: Объём чайника.
        :param is_on: Включен ли чайник в данный момент.

        :raise ValueError: Если заданный объём чайника не попадает в необходимый диапазон,
        то возвращается ошибка.

        Примеры:
        >>> kettle = Kettle(volume=1.5) # инициализация чайника
        """
        if volume <= 0 or volume > 5:
            raise ValueError("Объём чайника должен быть от 0 до 5 литров.")

        self.volume: float = volume  # В литрах
        self.is_on: bool = is_on
        self.water_level: float = 0  # Уровень воды в литрах

    def fill(self, amount: float) -> str:
        """
        Функция, которая заполняет чайник водой.
        :param amount: Количество добавляемой воды.

        :return: Текущий уровень воды в чайнике
        :raise ValueError: Если количество воды в чайнике задано отрицательным,
        то возвращается ошибка.
        :raise ValueError: Если объём имеющейся воды в чайнике и долитой больше объёма чайника,
        то возвращается ошибка.
        """
        if amount <= 0:
            raise ValueError("Количество воды должно быть положительным.")
        if self.water_level + amount > self.volume:
            raise ValueError("Невозможно залить больше, чем позволяет объём чайника.")
        self.water_level += amount
        return f"Чайник заполнен. Текущий уровень воды: {self.water_level} литров."

    def boil(self) -> str:
        """
        Функция, которая кипятит воду в чайнике.

        :return: Кипячение воды
        :raise ValueError: Если уровень воды в чайнике меньше или равен нулю,
        то возвращается ошибка.
        """
        if self.water_level <= 0:
            raise ValueError("Нельзя кипятить пустой чайник.")
        self.is_on = True
        return "Чайник кипятит воду."


if __name__ == "__main__":
    doctest.testmod()  # тестирование примеров, которые находятся в документации