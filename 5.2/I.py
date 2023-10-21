def find_nod(a: int, b: int):
    while a % b != 0:
        a, b = b, a % b
    return b


def find_nok(a: int, b: int):
    return (a * b) // find_nod(a, b)


def convert_to_frac(val):
    if isinstance(val, int | str):
        return Fraction(val)
    else:
        return val


class Fraction:
    def __init__(self, *args):
        if len(args) == 1:
            if isinstance(args[0], str):
                vals = args[0].split('/')
                if len(vals) > 1:
                    args = map(int, vals)
                else:
                    args = int(vals[0]), 1
            elif isinstance(args[0], int):
                args = args[0], 1

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
        other = convert_to_frac(other)
        nok = find_nok(self.denom, other.denom)
        return Fraction(nok * self.numer // self.denom + nok * other.numer // other.denom, nok)

    def __sub__(self, other):
        other = convert_to_frac(other)
        nok = find_nok(self.denom, other.denom)
        return Fraction(nok * self.numer // self.denom - nok * other.numer // other.denom, nok)

    def __iadd__(self, other):
        other = convert_to_frac(other)
        nok = find_nok(self.denom, other.denom)
        self.numer = nok * self.numer // self.denom + nok * other.numer // other.denom
        self.denom = nok
        self.__shorten()
        return self

    def __isub__(self, other):
        other = convert_to_frac(other)
        nok = find_nok(self.denom, other.denom)
        self.numer = nok * self.numer // self.denom - nok * other.numer // other.denom
        self.denom = nok
        self.__shorten()
        return self

    def __mul__(self, other):
        other = convert_to_frac(other)
        return Fraction(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        other = convert_to_frac(other)
        return self.__mul__(other.reverse())

    def __imul__(self, other):
        other = convert_to_frac(other)
        self.numer *= other.numer
        self.denom *= other.denom
        self.__shorten()
        return self

    def __itruediv__(self, other):
        other = convert_to_frac(other)
        return self.__imul__(other.reverse())

    def __gt__(self, other):
        other = convert_to_frac(other)
        nok = find_nok(self.denom, other.denom)
        if (nok // self.denom) * self.numer > (nok // other.denom) * other.numer:
            return True
        return False

    def __lt__(self, other):
        other = convert_to_frac(other)
        return not self.__gt__(other) and self.__ne__(other)

    def __eq__(self, other):
        other = convert_to_frac(other)
        nok = find_nok(self.denom, other.denom)
        if (nok // self.denom) * self.numer == (nok // other.denom) * other.numer:
            return True
        return False

    def __ne__(self, other):
        other = convert_to_frac(other)
        return not self.__eq__(other)

    def __ge__(self, other):
        other = convert_to_frac(other)
        if self.__gt__(other) or self.__eq__(other):
            return True
        return False

    def __le__(self, other):
        other = convert_to_frac(other)
        if self.__lt__(other) or self.__eq__(other):
            return True
        return False
