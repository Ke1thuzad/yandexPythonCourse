import numpy as np


def stairs(matrice):
    size = matrice.shape[0]
    helping = generate_helping_matrice(size)
    temp = np.eye(size, dtype='int16')
    res = [matrice @ temp]
    for i in range(size - 1):
        temp = temp @ helping
        res.append(matrice @ temp)
    return np.array(res)


def generate_helping_matrice(size):
    res = np.zeros((size, size), dtype='int16')
    for i in range(size - 1):
        res[i, i + 1] = 1
    res[-1, 0] = 1
    return res


print(stairs(np.arange(3)))
# print(generate_helping_matrice(3))

