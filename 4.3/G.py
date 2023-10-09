def same_type(f):
    def decorated(*args, **kwargs):
        if check_types_of_variables(*args):
            return f(*args, **kwargs)
        print('Обнаружены различные типы данных')

    return decorated


def check_types_of_variables(*vars):
    for i in range(len(vars) - 1):
        if not isinstance(vars[i], type(vars[i + 1])):
            return 0
    return 1


@same_type
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5.2) or 'Fail')
print(a_plus_b(7, '9') or 'Fail')
print(a_plus_b(-3, 5) or 'Fail')
