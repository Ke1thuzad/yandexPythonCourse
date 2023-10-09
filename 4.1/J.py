def merge(a: tuple, b: tuple):
    return sorting(a + b)


def sorting(x: tuple):
    res = list(x)
    while 1:
        k = 0
        for i in range(len(res) - 1):
            if res[i] > res[i + 1]:
                res[i + 1], res[i] = res[i], res[i + 1]
                k = 1
        if not k:
            return tuple(res)
