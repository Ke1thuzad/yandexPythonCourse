def make_equation(*coefficients):
    if len(coefficients) <= 1:
        return f'{coefficients[0]}'
    return f'({make_equation(*coefficients[:-1])}) * x + {coefficients[-1]}'


print(make_equation(5, 4, 3, 2, 1))