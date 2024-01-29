class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга \"{self._name}\". Автор: {self._author}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name, author)
        self._pages = pages

    @property
    def pages(self):
        return self._pages

    @pages.setter
    def pages(self, value: int):
        if not isinstance(value, int):
            raise TypeError(f"атрибут 'pages' должен быть типа int")
        if value <= 0:
            raise ValueError("атрибут 'pages' должен иметь значение больше 0")
        self._pages = value

    def __str__(self):
        return super().__str__() + f" Количество страниц: {self._pages}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, pages={self._pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: float):
        super().__init__(name, author)
        self._duration = duration

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value: int | float):
        if not isinstance(value, int | float):
            raise TypeError(f"атрибут 'duration' должен быть типа int либо float")
        if value <= 0:
            raise ValueError("атрибут 'duration' должен иметь значение больше 0")
        self._duration = value

    def __str__(self):
        return super().__str__() + f" Продолжительность: {self._duration}."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self._name!r}, author={self._author!r}, duration={self._duration!r})"
