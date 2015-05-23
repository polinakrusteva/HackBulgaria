def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def simplefraction(a, b):
    n = gcd(a, b)
    if a % b == 0:
        return a // b
    elif n != 1:
        while n != 1:
            a = a // n
            b = b // n
            n = gcd(a, b)
    return "{} / {}".format(a, b)


class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, other):
        a = simplefraction(self.numerator, self.denominator)
        b = simplefraction(other.numerator, other.denominator)
        return a == b

    def __add__(self, other):
        a = self.numerator * other.denominator + other.numerator * self.denominator
        b = self.denominator * other.denominator
        return simplefraction(a, b)

    def __sub__(self, other):
        a = self.numerator * other.denominator - other.numerator * self.denominator
        b = self.denominator * other.denominator
        return simplefraction(a, b)

    def __mul__(self, other):
        a = self.numerator * other.numerator
        b = self.denominator * other.denominator
        return simplefraction(a, b)
