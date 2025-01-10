# Менеджер задач
# Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты:
# описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
# отметки выполненных задач и вывода списка текущих (не выполненных) задач.

# Создаем класс Task
class Task():
    # Конструктор класса
    def __init__(self, description, deadline, status="No"):
        self.description = description  # Описание задачи
        self.deadline = deadline        # Срок исполнения
        self.status = status            # Статус (выполнено/не выполнено)

# Создаем класс Check для проверки корректного ввода даты
class Check():
    def __init__(self, date):
        self.date = date

    def check_date(self):
        if len(self.date) != 8 or self.date[2] != ":" or self.date[5] != ":":
            return False
        else:
            dd, mm, gg = self.date.split(':')
            if 1 <= int(dd) <= 31 and 1 <= int(mm) <= 12 and 0 <= int(gg) <= 99:
                return True
            else:
                return False

# Создаем класс Menager
class Menager():
    # Конструктор класса
    def __init__(self):
        self.task_list = []                                 # Список задач
        with open("task_list.txt", encoding="utf-8") as f:  # Читаем ранее сохраненные задачи
            while True:
                line = f.readline()
                if not line:
                    break
                line = line.strip("\n")                     # Удаляем разделитель строк (объектов класса Task) в файле
                description, deadline, status = line.split("#") # Выделяем из строки атрибуты класса Task
                task = Task(description, deadline, status)  # Создаем объект класса Task
                self.task_list.append(task)                 # Добавляем его в конец списка

    # Добавление задачи
    def add(self, description, deadline):
        task = Task(description, deadline)                  # Создаем объект класса Task
        self.task_list.append(task)                         # Добавляем его в конец списка
        print("Задача успешно добавлена")

    # Отметка о выполнении
    def completed(self, index):
        if 0 <= index < len(self.task_list):                # Проверяем корректность введенного индекса
            self.task_list[index].status = "Yes"
            print("Задача отмечена выполненой")
        else:
            print(f"Задачи с индексом {index} не существует")

    # Вывод текущих задач
    def print_tasks(self):
        for i in range(len(self.task_list)):                # Проходим по всем элементам списка
            if self.task_list[i].status == "No":            # Проверяем статус
                print(f"Индекс: {i} Задача: {self.task_list[i].description} Срок выполнения: {self.task_list[i].deadline}")

    # Сохранение задач в файл
    def exit(self):
        with open("task_list.txt", "w", encoding="utf-8") as f:
            for i in range(len(self.task_list)):
                f.write(self.task_list[i].description + "#" + self.task_list[i].deadline + "#" + self.task_list[i].status + "\n")

menager = Menager()                          # Создаем объект класса Menager

# Запускаем цикл общения с пользователем
while True:
    print("1 - Добавить задачу")
    print("2 - Отметить задачу выполненной")
    print("3 - Вывести список текущих задач")
    print("4 - Завершить программу")

    num = input("Выберите действие: ")

    match num:
        case "1":
            description = input("Введите задачу: ")
            while True:
                deadline = input("Введите срок выполнения в формате ДД:ММ:ГГ: ")
                obj = Check(deadline)
                print(obj.date)
                if not obj.check_date():
                    print("Неверный формат даты")
                else:
                    del obj
                    break
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


