def result_accumulator(f):
    queue = []

    def decorated(*args, method='accumulate', **kwargs):
        if method == 'accumulate':
            queue.append(f(*args, **kwargs))
        elif method == 'drop':
            queue.append(f(*args, **kwargs))
            results = queue.copy()
            queue.clear()
            return results

    return decorated



@result_accumulator
def a_plus_b(a, b):
    return a + b


print(a_plus_b(3, 5, method="accumulate"))
print(a_plus_b(7, 9))
print(a_plus_b(-3, 5, method="drop"))
print(a_plus_b(1, -7))
print(a_plus_b(10, 35, method="drop"))
