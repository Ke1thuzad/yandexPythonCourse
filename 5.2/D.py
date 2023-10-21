def find_nod(a: int, b: int):
    while a % b != 0:
        a, b = b, a % b
    return b


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            args = map(int, args[0].split('/'))
        numerator, denominator = args
        self.numer = numerator
        self.denom = denominator
        self.__shorten()

    def __shorten(self):
        nod = find_nod(self.numer, self.denom)
        self.numer //= nod
        self.denom //= nod

    def numerator(self, num=None):
        if num is None:
            return self.numer
        self.numer = num
        self.__shorten()
        return self

    def denominator(self, num=None):
        if num is None:
            return self.denom
        self.denom = num
        self.__shorten()
        return self

    def __str__(self):
        return f'{self.numer}/{self.denom}'

    def __repr__(self):
        return f"Fraction('{self.numer}/{self.denom}')"

    def __neg__(self):
        return Fraction(self.numer * -1, self.denom)


a = Fraction('-1/2')
b = -a
print(a, b, a is b)
b.numerator(-b.numerator())
a.denominator(-3)
print(a, b)
print(a.numerator(), a.denominator())
print(b.numerator(), b.denominator())
