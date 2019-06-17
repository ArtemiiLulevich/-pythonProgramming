import datetime
import pytz


class Account:
    """Simple account class with balance"""

    @staticmethod
    def _current_time():
        utc_time = datetime.datetime.utcnow()
        return pytz.utc.localize(utc_time)

    def __init__(self, name, balance):
        self._name = name
        self._balance = balance
        self._transaction_list = []
        print("Account created for " + self._name)

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.show_balance()
            self._transaction_list.append((Account._current_time(), amount, self._balance))

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self._transaction_list.append((Account._current_time(), -amount, self._balance))
        else:
            print("You don't have enough money.")
        self.show_balance()

    def show_balance(self):
        print("Balance is {}".format(self._balance))

    def show_transactions(self):
        for date, amount, balance in self._transaction_list:
            if amount > 0:
                tran_type = "deposit"
            else:
                tran_type = "withdrawn"
                amount *= -1
            print("{:6} {}. Balance {} on {} [local time was {}]".format(amount, tran_type, balance, date, date.astimezone()))


if __name__ == '__main__':
    artemiy = Account("Artemii", 0)
    artemiy.show_balance()

    artemiy.deposit(1000)
    artemiy.withdraw(500)
    artemiy.withdraw(501)

    artemiy.show_transactions()

    steph = Account("Stepth", 800)

    steph.deposit(100)
    steph.withdraw(200)
    steph.show_transactions()

    # balance = artemii.balance
    # print(balance)
