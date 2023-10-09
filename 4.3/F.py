# НЕ РАБОТАЕТ
def merge_sort(a: list):
    if len(a) <= 1:
        return a
    left = merge_sort(a[:len(a) // 2])
    right = merge_sort(a[len(a) // 2:])
    return min(left, right) + max(left, right)