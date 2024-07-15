# Разработай систему управления учетными записями пользователей для небольшой компании.
# Компания разделяет сотрудников на обычных работников и администраторов.
# У каждого сотрудника есть уникальный идентификатор (ID), имя и уровень доступа.
# Администраторы, помимо обычных данных пользователей, имеют дополнительный уровень доступа и могут
# добавлять или удалять пользователя из системы.
# 1.Класс `User*: Этот класс должен инкапсулировать данные о пользователе:
# ID, имя и уровень доступа ('user' для обычных сотрудников).
#
# 2.Класс Admin: Этот класс должен наследоваться от класса User. Добавь дополнительный атрибут уровня доступа,
# специфичный для администраторов ('admin'). Класс должен также содержать методы add_user и remove_user,
# которые позволяют добавлять и удалять пользователей из списка (представь, что это просто список экземпляров User).
#
# 3.Инкапсуляция данных: Убедись, что атрибуты классов защищены от прямого доступа и модификации снаружи.
# Предоставь доступ к необходимым атрибутам через методы (например, get и set методы).
class User():
    def __init__(self,id, name, access_level = 'посетитель'):
        self._id = id
        self._name = name
        self._access_level = access_level

    def get_id(self):
        return self._id
    def get_name(self):
        return self._name
    def get_access_level(self):
        return self._access_level

    def set_name(self, name):
        self._name = name

    def set_access_level(self, access_level):
        self._access_level = access_level

class Admin(User):
    def __init__(self, id, name, access_level = 'админ'):
        super().__init__(id, name, access_level)
        self._users = []
    def add_user(self, user):
        if isinstance(user, User):
            self._users.append(user)
            print(f'Пользователь {user.get_id()} {user.get_name()} добавлен в систему')

    def remove_user(self,user_id):
        for user in self._users:
            if user.get_id() == user_id:
                self._users.remove(user)
                print(f'Пользователь {user.get_id()} {user.get_name()} удален из системы')
                return
        print(f'Пользователь с ID {user_id} не найден в системе')


user1 = User(122, "Борис", 'пользователь')
user2 = User(1422, "Дрогон", 'пользователь')
admin1 = Admin(555, "Гога", 'админ')

admin1.add_user(user2)
admin1.add_user(user1)
admin1.remove_user(122)
