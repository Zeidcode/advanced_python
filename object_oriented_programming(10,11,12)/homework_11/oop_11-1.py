
import time

class MyString:
    """Класс Моя Строка, представляющий строку с информацией об авторе и времени создания."""

    def __init__(self, string, author):
        """
        Инициализирует объект Моя Строка.

        Аргументы:
        - string (str): Строка текста.
        - author (str): Имя автора строки.
        """
        self.string = string
        self.author = author
        self.creation_time = time.time()

    def __str__(self):
        """
        Возвращает строковое представление объекта Моя Строка.

        Возвращает:
        - str: Строковое представление объекта Моя Строка.
        """
        return f"Строка: {self.string}\nАвтор: {self.author}\nВремя создания: {self.creation_time}"


my_str = MyString("Привет, мир!", "Павел")
print(my_str)
