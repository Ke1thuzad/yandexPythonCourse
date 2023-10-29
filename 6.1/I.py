import numpy as np


def rotate(matrice: np.array, angle):
    return np.rot90(matrice, -1 * angle // 90)


print(rotate(np.arange(12).reshape(3, 4), 270))
