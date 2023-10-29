def merge(a: tuple, b: tuple):
    try:
        _ = iter(a)
        _ = iter(b)
    except TypeError:
        raise StopIteration
    if any(not isinstance(i, type((list(a) + list(b))[0])) for i in list(a) + list(b)):
        raise TypeError
    if list(a) != sorted(a) or list(b) != sorted(b):
        raise ValueError
    res = []
    i = 0
    j = 0
    m_i = 0
    m_j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            res.append(a[i])
            i += 1
            m_j = j
        elif a[i] > b[j]:
            res.append(b[j])
            m_i = i
            j += 1
    else:
        if i == len(a):
            res += b[m_j:]
        elif j == len(b):
            res += a[m_i:]
    return tuple(res)
