class Store():
    # Конструктор класса
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item, price):
        self.items[item] = price
        print(f"Товар {item} добавлен в ассортимент")

    def delete_item(self, item):
        print(f"Товар {self.items.pop(item)} удален из ассортимента")

    def get_price(self, item):
        return self.items.get('item')

    def new_price(self, item, price):
        self.items[item] = price

list_store = []


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
            description = input("Введите задачу: ")
            deadline = input("Введите срок выполнения в формате ДД:ММ:ГГ: ")
            menager.add(description, deadline)
        case "2":
            menager.print_tasks()
            index = int(input("Введите индекс выполненной задачи: "))
            menager.completed(index)
        case "3":
            menager.print_tasks()
        case "4":
            menager.exit()
            break
        case _:
            print("Такого действия нет. Повторите выбор.")