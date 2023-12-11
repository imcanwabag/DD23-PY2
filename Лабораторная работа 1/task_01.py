import doctest


class Car:
    def __init__(self, fuel_capacity: float, fuel_level: float):
        """
        Создание и подготовка к работе объекта "Автомобиль"

        :param fuel_capacity: Вместимость топливного бака
        :param fuel_level: Текущий уровень топлива в баке

        Примеры:
        >>> car = Car(60, 10)  # инициализация экземпляра класса
        """
        if not isinstance(fuel_capacity, (int, float)):
            raise TypeError("Вместимость топливного бака должна быть типа int или float")
        if fuel_capacity <= 0:
            raise ValueError("Вместимость топливного бака должна быть положительным числом")
        self.fuel_capacity = fuel_capacity

        if not isinstance(fuel_level, (int, float)):
            raise TypeError("Уровень топлива должен быть int или float")
        if fuel_level < 0:
            raise ValueError("Уровень топлива не может быть отрицательным числом")
        if fuel_level > fuel_capacity:
            raise ValueError("Уровень топлива не может превышать вместимость бака")
        self.fuel_level = fuel_level

    def is_empty_tank(self) -> bool:
        """
        Функция, которая проверяет, является ли бак пустым

        :return: Является ли бак пустым

        Примеры:
        >>> car = Car(60, 0)
        >>> car.is_empty_tank()
        True
        """
        return self.fuel_level == 0

    def add_fuel(self, fuel: float) -> None:
        """
        Заправка автомобиля.

        :param fuel: Объем добавляемого топлива
        :raise ValueError: Если количество добавляемого топлива превышает свободное место в баке, то вызываем ошибку

        Примеры:
        >>> car = Car(60, 10)
        >>> car.add_fuel(45)
        """
        if not isinstance(fuel, (int, float)):
            raise TypeError("Добавляемое топливо должно быть типа int или float")
        if fuel < 0:
            raise ValueError("Добавляемое топливо должно быть положительным числом")
        new_fuel_level = self.fuel_level + fuel
        if new_fuel_level > self.fuel_capacity:
            raise ValueError("Добавляемое топливо превышает свободное место в баке")
        self.fuel_level = new_fuel_level

    def consume_fuel(self, fuel: float) -> None:
        """
        Расход топлива автомобилем.

        :param fuel: Объем расходуемого топлива
        :raise ValueError: Если количество расходуемого топлива превышает текущий уровень топлива в баке,
        то вызывается ошибка.

        Примеры:
        >>> car = Car(60, 60)
        >>> car.consume_fuel(15)
        """
        if not isinstance(fuel, (int, float)):
            raise TypeError("Расходуемое топливо должно быть типа int или float")
        if fuel < 0:
            raise ValueError("Расходуемое топливо должно быть положительным числом")
        if fuel > self.fuel_level:
            raise ValueError("Расходуемое топливо превышает доступное количество в баке")
        self.fuel_level -= fuel


class Tree:
    def __init__(self, kind: str, height: float, growth_speed: float, max_height: float):
        """
        Создание и подготовка к работе объекта "Дерево"

        :param kind: Вид дерева
        :param height: Текущая высота
        :param growth_speed: Скорость роста
        :param max_height: Максимальная высота

        Примеры:
        >>> spruce = Tree("Ель", 0, 10, 5000)  # инициализация экземпляра класса
        """
        if not isinstance(kind, str):
            raise TypeError("Вид дерева должен быть типа str")
        if not kind:
            raise ValueError("Вид дерева не может быть пустой строкой")
        self.kind = kind

        if not isinstance(growth_speed, (int, float)):
            raise TypeError("Скорость роста должна быть типа int или float")
        if growth_speed <= 0:
            raise ValueError("Скорость роста должна быть положительным числом")
        self.growth_speed = growth_speed

        if not isinstance(height, (int, float)):
            raise TypeError("Текущая высота должна быть int или float")
        if height < 0:
            raise ValueError("Текущая высота не может быть отрицательным числом")
        if height > max_height:
            raise ValueError("Текущая высота не может быть больше максимальной высоты")
        self.height = height

        if not isinstance(max_height, (int, float)):
            raise TypeError("Максимальная высота должна быть int или float")
        if max_height < 0:
            raise ValueError("Максимальная высота не может быть отрицательным числом")
        if max_height < height:
            raise ValueError("Максимальная высота не может быть меньше текущей высоты")
        self.max_height = max_height

    def grow(self, years: int = 1) -> None:
        """
        Заправка автомобиля.

        :param years: Количество лет
        :raise ValueError: Если количество лет не является целым положительным числом, то вызываем ошибку

        Примеры:
        >>> spruce = Tree("Ель", 0, 10, 5000)
        >>> spruce.grow(10)
        """
        if not isinstance(years, int):
            raise TypeError("Количество лет должно быть типа int")
        if years < 0:
            raise ValueError("Количество лет должно быть неотрицательным числом")

        for _ in range(years):
            new_height = self.height + self.growth_speed
            if new_height <= self.max_height:
                self.height = new_height

    def show_info(self) -> None:
        """
        Вывод справочной информации о дереве.

        Примеры:
        >>> spruce = Tree("Ель", 0, 10, 5000)
        >>> spruce.grow(10)
        >>> spruce.show_info()
        Вид дерева: Ель
        Высота: 1.00 м.
        """
        height = self.height / 100
        print(f"Вид дерева: {self.kind}\nВысота: {height:.2f} м.")


class Warrior:
    def __init__(self, name: str, health: int, damage: int, distance: int):
        """
        Создание и подготовка к работе объекта "Воин"

        :param name: Имя
        :param health: Здоровье
        :param damage: Урон
        :param distance: Дистанция, в пределах которой может атаковать

        Пример:
        >>> warrior = Warrior("John", 100, 20, 5)
        """
        if not isinstance(name, str):
            raise TypeError("Имя должно быть типа str")
        if not name:
            raise ValueError("Имя не может быть пустой строкой")
        self.name = name

        if not isinstance(health, int):
            raise TypeError("Здоровье должна быть типа int")
        if health <= 0:
            raise ValueError("Здоровье должно быть положительным числом")
        self.health = health

        if not isinstance(damage, int):
            raise TypeError("Урон должен быть типа int")
        if damage <= 0:
            raise ValueError("Урон должен быть положительным числом")
        self.damage = damage

        if not isinstance(distance, int):
            raise TypeError("Дистанция должна быть типа int")
        if distance <= 0:
            raise ValueError("Дистанция должна быть положительным числом")
        self.distance = distance

    def strike(self, enemy, distance: int) -> None:
        """
        Нанесение удара по врагу

        :param enemy: Объект врага
        :param distance: Дистанция до врага

        Пример:
        >>> warrior = Warrior("John", 100, 20, 5)
        >>> victim = Warrior("Benjamin", 100, 10, 5)
        >>> warrior.strike(victim, 4)
        >>> victim.show_info()
        Имя: Benjamin
        Здоровье: 80
        """
        if distance <= self.distance:
            enemy.health -= self.damage

    def show_info(self) -> None:
        """
        Вывод информации о воине

        Пример:
        >>> warrior = Warrior("John", 100, 20, 5)
        >>> warrior.show_info()
        Имя: John
        Здоровье: 100
        """
        print(f"Имя: {self.name}\nЗдоровье: {self.health}")


if __name__ == "__main__":
    doctest.testmod()
