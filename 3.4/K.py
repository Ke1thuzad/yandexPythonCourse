from itertools import product


def solution(n: int, m: int):
    row = list(range(n))
    column = list(range(1, m + 1))
    max_len = len(str(n * m))
    for a, b in product(row, column):
        print(f'{a * m + b: >{max_len}}', end=' ')
        if b == m:
            print()


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
