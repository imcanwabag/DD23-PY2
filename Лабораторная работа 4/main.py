class Warrior:
    """
    Базовый класс, представляющий воина.
    """

    # Дистанция, в пределах которой воин может наносить урон
    DISTANCE = 10

    def __init__(self, name: str, health: int, damage: int):
        """
        Инициализация воина.

        :param name: Имя воина
        :param health: Здоровье воина
        :param damage: Урон, который может нанести воин
        """
        self.name = name
        self.damage = damage
        # Здоровье воина инкапсулировано для защиты от прямого изменения извне
        self.__health = health

    @property
    def health(self) -> int:
        """Возвращает текущее значение здоровья воина"""
        return self.__health

    def attack(self, enemy: 'Warrior', distance: int) -> None:
        """
        Атаковать врага

        :param enemy: Враг
        :param distance: Расстояние до врага
        """
        if self.is_alive() and enemy.is_alive() and distance <= self.DISTANCE:
            enemy.take_damage(self.damage)

    def take_damage(self, damage: int) -> None:
        """
        Получить урон

        :param damage: Количество полученного урона.
        """
        if self.is_alive():
            self.__health -= damage

    def is_alive(self) -> bool:
        """Проверка, жив ли воин."""
        return self.health > 0

    def __str__(self) -> str:
        """Возвращает строковое представление воина"""
        return f"Имя: {self.name}. Здоровье: {self.health}. Статус: {'Жив' if self.is_alive() else 'Мёртв'}."

    def __repr__(self) -> str:
        """Возвращает представление воина"""
        return f"{self.__class__.__name__}({self.name!r}, {self.health}, {self.damage})"


class Archer(Warrior):
    """
    Класс, представляющий лучника.
    """

    # Расстояние, в пределах которого лучник может наносить урон
    DISTANCE = 100

    def __init__(self, name: str, health: int, damage: int, arrows: int):
        """
        Инициализация лучника.

        :param name: Имя лучника
        :param health: Здоровье лучника
        :param damage: Урон, который может нанести лучник
        :param arrows: Количество стрел у лучника
        """
        super().__init__(name, health, damage)
        # Количество стрел инкапсулировано для контроля доступа
        self.__arrows = arrows

    # Перегружаем метод attack, чтобы уменьшать количество стрел при выстрелах
    def attack(self, enemy: 'Warrior', distance: int) -> None:
        """
        Атаковать врага

        :param enemy: Враг
        :param distance: Расстояние до врага
        """
        if self.has_arrows():
            super().attack(enemy, distance)
            self.__arrows -= 1

    @property
    def arrows(self) -> int:
        """Возвращает текущее количество стрел"""
        return self.__arrows

    def has_arrows(self) -> bool:
        """Проверка, имеются ли стрелы"""
        return self.arrows > 0

    # Перегружаем __str__, чтобы указать количество стрел
    def __str__(self) -> str:
        """Возвращает строковое представление лучника."""
        return super().__str__() + f" Количество стрел: {self.__arrows}."

    # Перегружаем __repr__, что отобразить изменения в конструкторе
    def __repr__(self) -> str:
        """Возвращает представление лучника."""
        return f"{self.__class__.__name__}({self.name!r}, {self.health}, {self.damage}, {self.arrows})"


if __name__ == "__main__":
    character1 = Warrior("Akira", 100, 50)
    character2 = Archer("Keita", 100, 25, 15)

    print(repr(character1))
    print(repr(character2))

    print("-" * 30)

    print(character1)
    print(character2)

    print("-" * 30)

    character2.attack(character1, 150)
    character2.attack(character1, 25)
    character2.attack(character1, 5)

    character1.attack(character2, 15)
    character1.attack(character2, 5)
    character1.attack(character2, 1)

    print(character1)
    print(character2)
