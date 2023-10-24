class NoSolutionsError(Exception):
    pass


class InfiniteSolutionsError(Exception):
    pass


def find_roots(a: float, b: float, c: float):
    if all(not isinstance(i, float | int) for i in (a, b, c)):
        raise TypeError
    elif not a and not b and not c:
        raise InfiniteSolutionsError
    elif not a and not b and c:
        raise NoSolutionsError
    elif not a:
        return -c / b, -c / b
    else:
        D = b ** 2 - 4 * a * c
        if D > 0:
            quadric_roots = sorted(((-b - D ** 0.5) / (2 * a), (-b + D ** 0.5) / (2 * a)))
            return tuple(quadric_roots)
        elif D == 0:
            return -b / (2 * a), -b / (2 * a)
        else:
            raise NoSolutionsError