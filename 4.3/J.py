def make_linear(lst: list):
    out = []
    for i in range(len(lst)):
        if isinstance(lst[i], list):
            return out + make_linear(lst[i] + lst[i + 1:])
        else:
            out.append(lst[i])
    return out


print(make_linear([1, [2, [3, 4]], [5, [7, [9, 10], 8]], 6]))