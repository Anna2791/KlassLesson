# Задание: Разработать консольную игру "Битва героев" на Python с использованием классов и разработать
# план проекта по этапам/или создать kanban доску для работы над данным проектом

# Общее описание: Создайте простую текстовую боевую игру, где игрок и компьютер управляют героями
# с различными характеристиками. Игра состоит из раундов, в каждом раунде игроки по очереди наносят
# урон друг другу, пока у одного из героев не закончится здоровье.

# Требования:
# Используйте ООП (Объектно-Ориентированное Программирование) для создания классов героев.
# Игра должна быть реализована как консольное приложение.
# # Классы:
# # Класс Hero:
# #     Атрибуты:
# #     Имя (name)
# #     Здоровье (health), начальное значение 100
# #     Сила удара (attack_power), начальное значение 20
# #     Методы:
# #     attack(other): атакует другого героя (other), отнимая здоровье в размере своей силы удара
# #     is_alive(): возвращает True, если здоровье героя больше 0, иначе False
# # Класс Game:
# #     Атрибуты:
# #     Игрок (player), экземпляр класса Hero
# #     Компьютер (computer), экземпляр класса Hero
# #     Методы:# #     start(): начинает игру, чередует ходы игрока и компьютера,
# пока один из героев не умрет. Выводит информацию о каждом ходе
# (кто атаковал и сколько здоровья осталось у противника) и объявляет победителя.
import random

class Hero:
    def __init__(self, name, health=100, attack_power=20):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, other):
        damage = random.randint(1, self.attack_power)
        other.health -= damage
        return damage
    def is_alive(self):
        if self.health > 0:
           return True
        else: False
class Game():
    def __init__(self, player_name, computer_name):
        self.player = Hero(player_name)
        self.computer = Hero(computer_name)

    def start(self):
        print(f'Игра начинается! {self.player.name} против {self.computer.name}')

        while self.player.is_alive() and self.computer.is_alive():

            print(f'Ход {self.player.name}')
            player_damage = self.player.attack(self.computer)
            print(f'{self.player.name} атаковал {self.computer.name} и нанес {player_damage} урона.')
            print(f'У {self.computer.name} осталось {self.computer.health} здоровья.')

            if not self.computer.is_alive():
                print(f'{self.computer.name} умер. {self.player.name} победил!')
                break


            print(f'Ход {self.computer.name}')
            computer_damage = self.computer.attack(self.player)
            print(f'{self.computer.name} атаковал {self.player.name} и нанес {computer_damage} урона.')
            print(f'У {self.player.name} осталось {self.player.health} здоровья.')

            if not self.player.is_alive():
                print(f'{self.player.name} умер. {self.computer.name} победил!')
                break

hero = Hero('Спанч боб', 100, 15)
computer = Hero('Система',100,24)
game = Game('Спанч боб','Система')
game.start()