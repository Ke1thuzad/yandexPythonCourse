from itertools import product


def solution(n: int):
    for a, b in product(range(1, n + 1), repeat=2):
        print(a * b, end=' ')
        if b == n:
            print()


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
