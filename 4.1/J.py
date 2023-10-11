def merge(a: tuple, b: tuple):
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