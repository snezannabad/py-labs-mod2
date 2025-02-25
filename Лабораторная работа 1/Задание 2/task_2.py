# TODO: импортируйте классы, созданные в ходе выполнения прошлого задания
from task_1 import Car, Laptop, Kettle


if __name__ == "__main__":
    car = Car(speed=40, power=1000)
    laptop = Laptop(brand="Redmi", battery_capacity=5100)
    kettle = Kettle(volume=2.5)
    # TODO: инстанцировать все описанные классы, создав три объекта.

    try:
        print(car.adjust_speed(-20))
        # TODO: вызвать метод с некорректными аргументами(b)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        print(laptop.gaming(-5))
        # TODO: вызвать метод с некорректными аргументами(a)
    except ValueError:
        print('Ошибка: неправильные данные')

    try:
        print(kettle.fill(6))
        # TODO: вызвать метод с некорректными аргументами(a)
    except ValueError:
        print('Ошибка: неправильные данные')


