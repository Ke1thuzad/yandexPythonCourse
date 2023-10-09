def gcd(*values):
    if len(values) <= 1:
        return values[0]
    last_nod = find_nod(values[0], values[1])
    for i in range(2, len(values)):
        last_nod = find_nod(last_nod, values[i])
    return last_nod


def find_nod(a: int, b: int):
    remainder = a % b
    while remainder != 0:
        a, b = b, remainder
        remainder = a % b
    return b