def solution(val: int):
    mx = [0, 0]
    for i in range(2, 11):
        b = count_digits(to_base(val, i))
        if b > mx[1]:
            mx = [i, b]

    print(mx[0])


def to_base(x: int, base: int):
    total = ''
    while x > 0:
        total += str(x % base)
        x //= base
    return int(total)


def count_digits(x: int):
    result = 0
    while x > 0:
        result += x % 10
        x //= 10
    return result


def main():
    val = int(input())
    solution(val)


if __name__ == '__main__':
    main()
