def cycle(lst: list):
    i = 0
    while 1:
        yield lst[i]
        i += 1
        i %= len(lst)


print(*(x for _, x in zip(range(5), cycle([1, 2, 3]))))
