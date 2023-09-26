from itertools import chain


def solution(wanted: list):
    for i, product in enumerate(wanted, 1):
        print(f'{i}. {product}')


def main():
    n = int(input())
    wanted = [input().split(', ') for _ in range(n)]
    wanted = chain.from_iterable(wanted)
    solution(sorted(wanted))


if __name__ == '__main__':
    main()
