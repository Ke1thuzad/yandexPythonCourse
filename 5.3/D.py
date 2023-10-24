def only_positive_even_sum(a: int, b: int):
    if not isinstance(a, int) and not isinstance(b, int):
        raise TypeError
    elif a % 2 != 0 or a < 0 or b < 0 or b % 2 != 0:
        raise ValueError
    else:
        print(a + b)