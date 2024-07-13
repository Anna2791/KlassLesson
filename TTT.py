# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети
# имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и
# ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для
# создания различных магазинов. метод для добавления товара в ассортимент.метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.метод для обновления цены товара

class Store():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f'Добавлен товар - {item_name} с ценой {price}')

    def delete_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f'Товар удален - {item_name}')
        else:
            print(f'Товар {item_name} не найден')

    def get_price(self, item_name):
        if item_name in self.items:
            price = self.items[item_name]
            print(f'Цена запрашиваемого товара {item_name} составляет {price}')
            return price
        else:
            return None


    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f'Новая цена товара {item_name} - {new_price}')



store1 = Store('Пятерочка', 'Восточный 52')
store2 = Store('Мусьена', 'Вологодская 5')
store3 = Store('Радуга', 'Пролетарская 3')


store1.add_item('содовая', 20)
store2.add_item('apples', 15)
store3.add_item('банан', 10)

store1.delete_item('содовая')

print(store2.get_price('apples'))


store3.update_price('банан', 12)


print(store3.get_price('банан'))

# Выбери один из созданных магазинов и протестируй все его методы:
# добавь товар, обнови цену, убери товар и запрашивай цену.
store3.add_item('apples', 99)
store3.update_price('банан',34)
store3.get_price('apples')
store3.delete_item('банан')
