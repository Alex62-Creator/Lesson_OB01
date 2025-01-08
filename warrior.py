class Warrior():
    def __init__(self, name, hair_color, power, endurance):
        self.name = name
        self.power = power
        self.endurance = endurance
        self.hair_color = hair_color

    def eat(self):
        print(f"{self.name} решил поесть")
        self.power += 1

    def sleep(self):
        print(f"{self.name} решил поспать")
        self.endurance += 2

    def hit(self):
        print(f"{self.name} решил подраться")
        self.endurance -= 5

    def walk(self):
        print(f"{self.name} решил погулять")

    def info(self):
        print(f"Наш герой - {self.name}")
        print(f"Имеет цвет волос - {self.hair_color}")
        print(f"Сейчас у него сила - {self.power}")
        print(f"Сейчас у него выносливость - {self.endurance}")

war1 = Warrior("Скиф", "руссый", 65, 89)
war2 = Warrior("Викинг", "рыжий", 95, 59)

war1.info()
war1.eat()
war1.sleep()
war1.hit()
war1.walk()
war1.info()

war2.info()
war2.eat()
war2.sleep()
war2.hit()
war2.walk()
war2.info()