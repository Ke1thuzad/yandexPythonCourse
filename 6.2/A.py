import pandas as pd


def length_stats(text: str):
    formatted_text = ''.join([i.lower() for i in text if i.isalpha() or i == ' '])
    return pd.Series({i: len(i) for i in sorted(formatted_text.split())})
