class Account():
    def __init__(self, id, ballance=0):
        self.id = id
        self.ballance = ballance

    def deposit(self, money):
        if money > 0:
            self.ballance += money
            print(f"Вы успешно пополнили свой счет на {money} рублей. Текущее состояние счета: {self.ballance}")

    def withdraw(self, money):
        if money > self.ballance:
            print("Недостаточно средств на счете")
        else:
            self.ballance -= money
            print(f"Вы успешно сняли со счета {money} рублей. Текущее состояние счета: {self.ballance}")

    def current_ballance(self):
        print(f"Текущее состояние счета: {self.ballance}")

client = Account("123456", 5000)

client.current_ballance()
client.withdraw(2500)
client.withdraw(3000)
client.deposit(25000)