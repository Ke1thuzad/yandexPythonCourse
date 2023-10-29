import pandas as pd


def length_stats(text: str):
    formatted_text = ''.join([i.lower() for i in text if i.isalpha() or i == ' '])
    formatted_text = sorted(formatted_text.split())
    odd = pd.Series({i: len(i) for i in formatted_text if len(i) % 2}, dtype='int64')
    even = pd.Series({i: len(i) for i in formatted_text if len(i) % 2 == 0}, dtype='int64')
    return odd, even
