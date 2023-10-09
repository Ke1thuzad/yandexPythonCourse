def make_equation(*coefficients):
    if not coefficients:
        return ''
    return make_equation(*coefficients[:-1]) + f' + {coefficients[-1]}'


print(make_equation(1, 2, 3))
