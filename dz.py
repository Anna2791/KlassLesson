# Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.
# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут
# иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()`
# для `Veterinarian`).
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print('РрррРРРРРррр')

    def eat(self):
        print('ном-ном-ном')

class Bird(Animal):
    def __init__(self, color):
        self.color = color
    def make_sound(self):
        print('чирик')

class Mammal(Animal):
    def __init__(self, size):
        self.size = size
    def make_sound(self):
        print('няяяя')
class Reptile(Animal):
    def make_sound(self):
        print('ссссссссссссс')

def animal_sound(self):
    self.animals = [Bird('белая'), Mammal('большой'),Animal('ворон', 2), Reptile()]
    for animal in self.animals:
        animal.make_sound()


animal = Animal('лев',2)
bird = Bird('черная')
animal.eat()
animal.make_sound()
bird.make_sound()
animal.animal_sound