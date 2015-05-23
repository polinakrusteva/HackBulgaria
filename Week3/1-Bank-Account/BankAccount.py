class BankAccount:
    def __init__(self, name, balance, currency):
        self.__name = name
        self.__balance = balance
        self.__currency = currency
        self.__history = ["Account was created"]
        if balance < 0:
            raise ValueError

    def __str__(self):
        return "Bank account for {} with balance of {}{}".format(self.name, self.balance, self.currency)

    def __int__(self):
        self.__history.append("__int__ check -> {}{}".format(self.__balance, self.__currency))
        return self.__balance

    def balance(self):
        self.__history.append("Balance Check -> {}{}".format(self.__balance, self.__currency))
        return self.__balance

    def deposit(self, amount):
        result = self.__balance + amount
        self.__history.appen("Deposited {}{}".format(amount, self.__currency))
        return result

    def withdraw(self, amount):
        if self.__balance - amount < 0:
            self.__history.append("Withdraw for {}{} failed".format(amount, self.__currency))
            return False
        self.__balance = self.__balance - amount
        self.__history.append("{}{} was withdrawed".format(amount, self.__currency))
        return True

    def transfer_to(self, account, amount):
        if isinstance(account, BankAccount):
            if self.__currency != account.__currency:
                return False
        self.__balance = self.__balance - amount
        account.__balance = account.__balance + amount
        self.__history.append("Transfer to {} for {}{}".format(account.__name, amount, self.__currency))
        account.__history.append("Transfer from {} for {}{}".format(self.__name, amount, self.__currency))
        return True

    def history(self):
        return self.__history

rado = BankAccount("Rado", 1000, "BGN")
ivo = BankAccount("Ivo", 0, "BGN")
print(rado.transfer_to(ivo, 500))
print(rado.balance())
print(ivo.balance())
print(rado.history())
print(ivo.history())
