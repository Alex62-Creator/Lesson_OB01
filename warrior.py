class Warrior():
    def __init__(self, name, power, hair_color, endurance):
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

    def bit(self):
        print(f"{self.name} решил подраться")
        self.endurance -= 5

    def walk(self):
        print(f"{self.name} решил погулять")

    def info(self):
        print(f"Наш герой - {self.name}")
        print(f"Имеет цвет волос - {self.hair_color}")
        print(f"Сейчас у него сила - {self.power}")
        print(f"Сейчас у него выносливость - {self.endurance}")