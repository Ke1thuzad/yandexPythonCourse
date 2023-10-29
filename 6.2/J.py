import pandas as pd
import numpy as np


def values(func, start, end, step):
    return pd.Series({i: func(i) for i in np.arange(start, end, step)})


def min_extremum(data):
    return data.idxmin()


def max_extremum(data):
    return data.idxmax()
