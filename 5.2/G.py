def find_nod(a: int, b: int):
    while a % b != 0:
        a, b = b, a % b
    return b


def find_nok(a: int, b: int):
    return (a * b) // find_nod(a, b)


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

    def reverse(self):
        return Fraction(self.denom, self.numer)

    def __str__(self):
        return f'{self.numer}/{self.denom}'

    def __repr__(self):
        return f"Fraction('{self.numer}/{self.denom}')"

    def __neg__(self):
        return Fraction(self.numer * -1, self.denom)

    def __add__(self, other):
        nok = find_nok(self.denom, other.denom)
        return Fraction(nok * self.numer // self.denom + nok * other.numer // other.denom, nok)

    def __sub__(self, other):
        nok = find_nok(self.denom, other.denom)
        return Fraction(nok * self.numer // self.denom - nok * other.numer // other.denom, nok)

    def __iadd__(self, other):
        nok = find_nok(self.denom, other.denom)
        self.numer = nok * self.numer // self.denom + nok * other.numer // other.denom
        self.denom = nok
        self.__shorten()
        return self

    def __isub__(self, other):
        nok = find_nok(self.denom, other.denom)
        self.numer = nok * self.numer // self.denom - nok * other.numer // other.denom
        self.denom = nok
        self.__shorten()
        return self

    def __mul__(self, other):
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return self.__mul__(other.reverse())

    def __imul__(self, other):
        self.numer *= other.numer
        self.denom *= other.denom
        self.__shorten()
        return self

    def __itruediv__(self, other):
        return self.__imul__(other.reverse())
