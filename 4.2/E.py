def to_string(*values, sep: str = ' ', end: str = '\n'):
    return sep.join(map(str, values)) + end