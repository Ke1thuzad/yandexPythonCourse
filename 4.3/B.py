def recursive_digit_sum(num: int):
    if not num:
        return 0
    return num % 10 + recursive_digit_sum(num // 10)