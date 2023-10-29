import pandas as pd


def get_long(serie: pd.Series, min_length=5):
    return serie[serie >= min_length]
