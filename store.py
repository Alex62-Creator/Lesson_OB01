class Store():
    # Конструктор класса
    def __init__(self, name, address):
        self.name = name                # Название магазина
        self.address = address          # Адрес магазина
        self.items = {}                 # Ассортимент магазина (товар - ключ, значение - цена)

    # Добавление товара
    def add_item(self, item, price):
        self.items[item] = price
        print(f"Товар {item} добавлен в ассортимент")

    # Удаление товара
    def delete_item(self, item):
        if item not in self.items:
            print(f"Товар {item} отсутствует в ассортименте этого магазина")
        else:
            del self.items[item]
            print(f"Товар {item} удален из ассортимента")

    # Получение цены товара
    def get_price(self, item):
        if item not in self.items:
            print(f"Товар {item} отсутствует в ассортименте этого магазина")
        else:
            print(f"Цена {item} - {self.items[item]} рублей")

    # Изменение цены товара
    def new_price(self, item, price):
        if item not in self.items:
            print(f"Товар {item} отсутствует в ассортименте этого магазина")
        else:
            self.items[item] = price
            print(f"Новая цена товара {item} - {price} рублей")

list_store = []                         # Список магазинов (каждый элемент - объект класса Store
ind = None                              # Индекс магазина в списке, с которым производятся действия

# Запускаем цикл общения с пользователем
while True:
    print("1 - Добавить магазин")
    print("2 - Вывести список магазинов нашей сети")
    print("3 - Выбрать магазин для работы")
    print("4 - Добавить товар")
    print("5 - Удалить товар")
    print("6 - Узнать цену товара")
    print("7 - Поменять цену товара")
    print("8 - Завершить программу")

    num = input("Выберите действие: ")

    match num:
        case "1":
            ind = None
            shop = input("Ведите название магазина: ")
            address = input("Ведите адрес магазина: ")
            store = Store(shop, address)
            list_store.append(store)
            print(f"Магазин {shop} добавлен в нашу сеть")
        case "2":
            ind = None
            print("Список магазинов нашей сети:")
            for i, shop in enumerate(list_store):
                print(f"{i + 1} {list_store[i].name}")
        case "3":
            ind = None
            for i, shop in enumerate(list_store):
                print(f"{i + 1} {list_store[i].name}")
            ind = int(input("Введите номер в списке интересующего вас магазина: ")) - 1
        case "4":
            if ind == None:
                print("Вы не выбрали магазин для работы. Для начала выберите пункт 3 из меню")
            elif 0 <= ind < len(list_store):
                item = input("Введите наименование товара: ")
                price = input("Введите цену товара: ")
                list_store[ind].add_item(item, price)
            else:
                print("Вы неправильно выбрали магазин для работы. Для начала повторите пункт 3 из меню")
        case "5":
            if ind == None:
                print("Вы не выбрали магазин для работы. Для начала выберите пункт 3 из меню")
            elif 0 <= ind < len(list_store):
                item = input("Введите наименование товара, который вы хотитите удалить: ")
                list_store[ind].delete_item(item)
            else:
                print("Вы неправильно выбрали магазин для работы. Для начала повторите пункт 3 из меню")
        case "6":
            if ind == None:
                print("Вы не выбрали магазин для работы. Для начала выберите пункт 3 из меню")
            elif 0 <= ind < len(list_store):
                item = input("Введите наименование товара, цену которого вы хотите узнать: ")
                list_store[ind].get_price(item)
            else:
                print("Вы неправильно выбрали магазин для работы. Для начала повторите пункт 3 из меню")
        case "7":
            if ind == None:
                print("Вы не выбрали магазин для работы. Для начала выберите пункт 3 из меню")
            elif 0 <= ind < len(list_store):
                item = input("Введите наименование товара, цену которого вы хотите изменить: ")
                price = input(f"Введите новую цену {item}: ")
                list_store[ind].new_price(item, price)
            else:
                print("Вы неправильно выбрали магазин для работы. Для начала повторите пункт 3 из меню")
        case "8":
            break
        case _:
            print("Такого действия нет. Повторите выбор.")