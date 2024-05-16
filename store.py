class Store:
    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        self.items = {} if items is None else items


    def add_item(self, item_name, price):
        self.items[item_name] = price
        print(f"Товар {item_name} был добавлен в магазин {self.name} по адресу {self.address} с ценой {price}")
    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]
            print(f"Товар {item_name} был удален из магазина {self.name} по адресу {self.address}")
        else:
            print(f"Товар {item_name} не был найден в магазине {self.name} по адресу {self.address}")

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price
            print(f"Товар {item_name} был обновлен в магазине {self.name} по адресу {self.address} на цену {new_price} ")
        else:
            print(f"Товар {item_name} не был найден в магазине {self.name} по адресу {self.address}")
    def get_price(self, item_name):
        if item_name in self.items:
            return self.items[item_name]
        else:
            return None
store1 = Store("Магазин 1", "Тверская д 4", {"Яблоки": 100, "Бананы": 200, "Груши": 150})
store2 = Store("Магазин 2", "Нагатинская д 2", {"Яблоки": 120, "Апельсины": 200, "Виноград": 300})
store3 = Store("Магазин 3", "Бутова д 3", {"Лимоны": 350, "Апельсины": 220, "Виноград": 300})
print(f"Товары в магазине {store1.name} по адресу {store1.address}:", store1.items)
store1.add_item("Виноград", 300)
print(f"Товары в магазине {store1.name} по адресу {store1.address}:", store1.items)
print(f"Товары в магазине {store2.name} по адресу {store2.address}:", store2.items)
store2.update_price("Виноград", 450)
print(f"Товары в магазине {store2.name} по адресу {store2.address}:", store2.items)
print(f"Товары в магазине {store3.name} по адресу {store3.address}:", store3.items)
store3.remove_item("Лимоны")
print(f"Товары в магазине {store3.name} по адресу {store3.address}:", store3.items)
print(f"Товары в магазине {store3.name} по адресу {store3.address}:", store3.items)
price = store1.get_price("Яблоки")
if price is None:
    print(f"Товар 'Яблоки' не был найден в магазине {store1.name} по адресу {store1.address}")
else:
    print(f"Цена товара 'Яблоки' в магазине {store1.name} по адресу {store1.address}: {price}")
price = store3.get_price("Яблоки")
if price is None:
    print(f"Товар 'Яблоки' не был найден в магазине {store3.name} по адресу {store3.address}")
else:
    print(f"Цена товара 'Яблоки' в магазине {store3.name} по адресу {store3.address}: {price}")
store3.get_price("Яблоки")


