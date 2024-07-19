# Создайте базовый класс `Animal`, который будет содержать общие атрибуты
# (например, `name`, `age`) и методы (`make_sound()`, `eat()`) для всех животных.
# Реализуйте наследование, создав подклассы `Bird`, `Mammal`, и `Reptile`,
# которые наследуют от класса `Animal`. Добавьте специфические атрибуты и
# переопределите методы, если требуется (например, различный звук для `make_sound()`).
# 3. Продемонстрируйте полиморфизм: создайте функцию `animal_sound(animals)`,
# которая принимает список животных и вызывает метод `make_sound()` для каждого животного.


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        print('РрррРРРРРррр')

    def eat(self):
        print('ном-ном-ном')

class Bird(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print('чирик')

class Mammal(Animal):
    def __init__(self, name, age, size):
        super().__init__(name, age)
        self.size = size

    def make_sound(self):
        print('няяяя')

class Reptile(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def make_sound(self):
        print('ссссссссссссс')


def animal_sound(animals):
    for animal in animals:
        animal.make_sound()
def info_animal(animals):
    for animal in animals:
        print(f'{animal.name} - {animal.age} лет')

# 4. Используйте композицию для создания класса `Zoo`, который будет содержать информацию
# о животных и сотрудниках. Должны быть методы для добавления животных и сотрудников в зоопарк.
# 5. Создайте классы для сотрудников, например, `ZooKeeper`, `Veterinarian`, которые могут
# иметь специфические методы (например, `feed_animal()` для `ZooKeeper` и `heal_animal()`
# для `Veterinarian`)
class Zoo():
    def __init__(self):
        self.animals = []
        self.employees = []
    def info(self):
        info_animal(self.animals)

    def add_animal(self,animal):
       self.animals.append(animal)
       print(f'{animal.name} добавлен в зоопарк')
    def add_employee(self,employee):
        self.employees.append(employee)
        print(f'{employee.name} добавлен в зоопарк')
class ZooKeeper():
    def __init__(self,name):
        self.name = name

    def feed_animal(self,animal):
        print(f'Зоокипер {self.name} кормит {animal.name}')
class Veterinarian():
    def __init__(self, name):
        self.name = name

    def heal_animal(self, animal):
        print(f'Ветеринар {self.name} лечит {animal.name}')




animal1 = Animal('Лев', 2)
bird = Bird('Воробей', 1, 'черная')
mammal = Mammal('Слон', 10, 'большой')
reptile = Reptile('Змея', 3)

zoo = Zoo()
zoo.add_animal(animal1)
zoo.add_animal(bird)
zoo.add_animal(mammal)
zoo.add_animal(reptile)

zookeeper = ZooKeeper('Грег')
veterinarian = Veterinarian('Шарлотта')
zoo.add_employee(zookeeper)
zoo.add_employee(veterinarian)

animals = [animal1, bird, mammal, reptile]
animal_sound(animals)
zoo.info()
zookeeper.feed_animal(animal1)
veterinarian.heal_animal(reptile)

