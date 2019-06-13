import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_list = []
        print("Account created for " + self.name)

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.show_balance()
            self.transaction_list.append((Account._current_time(), amount))

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            self.transaction_list.append((Account._current_time(), -amount))
        else:
            print("You don't have enough money.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self.balance))

    def show_transactions(self):
        for date, amount in self.transaction_list:
            if amount > 0:
                tran_type = "deposit"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {} on {} [local time was {}]".format(amount, tran_type, date, date.astimezone()))


if __name__ == '__main__':
    artemiy = Account("Artemii", 0)
    artemiy.show_balance()

    artemiy.deposit(1000)
    artemiy.withdraw(500)
    artemiy.withdraw(501)

    artemiy.show_transactions()
    # balance = artemii.balance
    # print(balance)
