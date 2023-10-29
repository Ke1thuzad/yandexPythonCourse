import pandas as pd


def best(students: pd.DataFrame):
    return students[(students['maths'] > 3) & (students['physics'] > 3) & (students['computer science'] > 3)]
