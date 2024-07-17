# Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
class Animal():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def make_sound(self):
        print('РрррРРРРРррр')

    def eat(self):
        print('ном-ном-ном')

animal = Animal('лев',2)
animal.eat()
animal.make_sound()