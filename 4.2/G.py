def enter_results(*results):
    global entered
    if entered is None:
        entered = []
    entered += [(results[i], results[i + 1]) for i in range(0, len(results), 2)]


def get_sum():
    left = sum([entered[i][0] for i in range(len(entered))])
    right = sum([entered[i][1] for i in range(len(entered))])
    return left, right


def get_average():
    left = round(sum([entered[i][0] for i in range(len(entered))]) / len(entered), 2)
    right = round(sum([entered[i][1] for i in range(len(entered))]) / len(entered), 2)
    return left, right


# entered = []
enter_results(1, 2, 3, 4, 5, 6)
print(get_sum(), get_average())
enter_results(1, 2)
print(get_sum(), get_average())