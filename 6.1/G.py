import numpy as np


def make_board(size: int):
    part_amount = size // 2
    part = np.eye(2, 2, dtype='int8')
    all_parts = np.concatenate([part for _ in range(part_amount)])
    return all_parts @ all_parts.transpose()


print(make_board(4))