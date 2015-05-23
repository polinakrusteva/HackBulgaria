class Bill:

    def __init__(self, amount):
        self.amount = amount

    def __str__(self):
        return "A {}$ bill".format(self.amount)

    def __repr__(self):
        return self.__str__()

    def __int__(self):
        return self.amount

    def __eq__(self, other):
        return self.amount == other.amount

    def __hash__(self):
        return hash(self.__str__())


class BillBatch:

    def __init__(self, bills):
        self.bills = bills

    def __len__(self):
        return len(self.bills)

    def __getitem__(self, index):
        return self.bills[index]

    def total(self):
        return sum([int(bill) for bill in self.bills])


class CashDesk:
    def __init__(self):
        self.gold = 0
        self.money_holder = {}

    def addmoney(self, money):
        if isinstance(money, Bill):
            if money in self.money_holder:
                self.money_holder[money] += 1
            else:
                self.money_holder[money] = 1
        elif isinstance(money, BillBatch):
            for bill in money:
                if bill in self.money_holder:
                    self.money_holder[bill] += 1
                else:
                    self.money_holder[bill] = 1

    def take_money(self, money):
        self.addmoney(money)
        if isinstance(money, Bill):
            self.gold += int(money)
        elif isinstance(money, BillBatch):
            self.gold += money.total()

    def total(self):
        return self.gold 

    def inspect(self):
        return self.money_holder
