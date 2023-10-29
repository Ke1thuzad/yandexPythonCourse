import numpy as np


def snake(m: int, n: int, direction='H'):
    res = np.arange(1, n * m + 1, dtype='int32')
    if direction == 'H':
        res.resize((n, m))
    else:
        res.resize((m, n))

    if direction == 'H':
        for i in range(n):
            if i % 2:
                res[i] = res[i][::-1]
    else:
        for i in range(m):
            if i % 2:
                res[i] = res[i][::-1]
        res = res.transpose()
    return res


snake(5, 3, 'V')