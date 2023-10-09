def answer(f):
    def decorated(*args, **kwargs):
        print(f'Результат функции: {f(*args, **kwargs)}')
    return decorated
