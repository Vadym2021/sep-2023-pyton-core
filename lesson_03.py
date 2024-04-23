# Створити клас Rectangle:
# -він має приймати дві сторони x,y
# -описати поведінку на арифметични методи:
# + сумма площин двох екземплярів ксласу
# - різниця площин двох екземплярів ксласу
# == площин на рівність
# != площин на не рівність
# >, < меньше більше
# при виклику метода len() підраховувати сумму сторін
#
class Rectangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def area(self):
        return self.x * self.y

    def __add__(self, other):
        return self.area() + other.area()

    def __sub__(self, other):
        return self.area() - other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __ne__(self, other):
        return self.area() != other.area()

    def __lt__(self, other):
        return self.area() < other.area()

    def __gt__(self, other):
        return self.area() > other.area()

    def __len__(self):
        return self.x + self.y
rect1 = Rectangle(5, 10)
rect2 = Rectangle(3, 7)

print("сумма площин двох екземплярів ксласу:", rect1 + rect2)
print("різниця площин двох екземплярів ксласу:", rect1 - rect2)
print("площин на рівність:", rect1 == rect2)
print("площин на не рівність:", rect1 != rect2)
print("меньше більше:", rect1 < rect2)
print("більше меньше:", rect1 > rect2)
print("сумму сторін rect1:", len(rect1))
print("сумму сторін rect2:", len(rect2))

print('-' * 40)

# ###############################################################################
#
# створити класс Human (name, age)
# створити два класси Prince и Cinderella які наслідуються від Human:
# у попелюшки мае бути ім'я, вік, розмір нонги
# у принца має бути ім'я, вік, та розмір знайденого черевичка, а також метод котрий буде приймати список попелюшок, та шукати ту саму
#
# в класі попелюшки має бути count який буде зберігати кількість створених екземплярів классу
# також має бути метод классу який буде виводити це значення
#
class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Cinderella(Human):
    count = 0

    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size
        Cinderella.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

class Prince(Human):
    def __init__(self, name, age, shoe_size):
        super().__init__(name, age)
        self.shoe_size = shoe_size

    def find_cinderella(self, cinderellas):
        for cinderella in cinderellas:
            if cinderella.shoe_size == self.shoe_size:
                return cinderella
        return None

# Приклад використання
cinderella1 = Cinderella("Cinderella1", 20, 35)
cinderella2 = Cinderella("Cinderella2", 21, 36)
cinderella3 = Cinderella("Cinderella3", 22, 37)

prince = Prince("Prince", 25, 37)

cinderellas = [cinderella1, cinderella2, cinderella3]

found_cinderella = prince.find_cinderella(cinderellas)
if found_cinderella:
    print(f"Found Cinderella: {found_cinderella.name}")
else:
    print("Cinderella not found")

print("Cinderella count:", Cinderella.get_count())

print('-' * 40)

#
# ###############################################################################
#
# 1) Створити абстрактний клас Printable який буде описувати абстрактний метод print()
# 2) Створити класи Book та Magazine в кожного в конструкторі змінна name, та який наслідуются від класу Printable
# 3) Створити клас Main в якому буде:
# - змінна класу printable_list яка буде зберігати книжки та журнали
# - метод add за допомогою якого можна додавати екземпляри класів в список і робити перевірку чи то що передають є класом Book або Magazine инакше ігрнорувати додавання
#  - метод show_all_magazines який буде виводити всі журнали викликаючи метод print абстрактного классу
from abc import ABC, abstractmethod

class Printable(ABC):
    @abstractmethod
    def print(self):
        pass

class Book(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Book: {self.name}")

class Magazine(Printable):
    def __init__(self, name):
        self.name = name

    def print(self):
        print(f"Magazine: {self.name}")

class Main:
    printable_list = []

    @classmethod
    def add(cls, item):
        if isinstance(item, (Book, Magazine)):
            cls.printable_list.append(item)


    @classmethod
    def show_all_magazines(cls):
        for item in cls.printable_list:
            if isinstance(item, Magazine):
                item.print()

    @classmethod
    def show_all_books(cls):
        for item in cls.printable_list:
            if isinstance(item, Book):
                item.print()


Main.add(Magazine('Magazine1'))
Main.add(Book('Book1'))
Main.add(Magazine('Magazine3'))
Main.add(Magazine('Magazine2'))
Main.add(Book('Book2'))

Main.show_all_magazines()
print('-' * 20)
Main.show_all_books()


#
# Приклад:
#
# Main.add(Magazine('Magazine1'))
# Main.add(Book('Book1'))
# Main.add(Magazine('Magazine3'))
# Main.add(Magazine('Magazine2'))
# Main.add(Book('Book2'))
#
# Main.show_all_magazines()
# print('-' * 40)
# Main.show_all_books()
#
#
# для перевірки ксассів використовуємо метод isinstance, приклад:
#
#
# user = User('Max', 15)
# shape = Shape()
#
# isinstance(max, User) -> True
# isinstance(shape, User) -> False
