import numpy as np


def multiplication_matrix(size: int):
    return np.array([np.arange(1, size + 1) * i for i in range(1, size + 1)])


print(multiplication_matrix(3))
