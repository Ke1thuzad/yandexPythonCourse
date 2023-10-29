import pandas as pd


def need_to_work_better(students: pd.DataFrame):
    return students[(students['maths'] == 2) | (students['physics'] == 2) | (students['computer science'] == 2)]