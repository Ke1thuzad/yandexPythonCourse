def is_palindrome(a):
    if isinstance(a, int):
        return str(a) == str(a)[::-1]
    if isinstance(a, str):
        return a == a[::-1]
    for i in range(len(a) // 2):
        if a[i] != a[-(i + 1)]:
            return False
    return True


result = is_palindrome(('1', '0', '1'))

print(result)