from itertools import chain, permutations


def solution(wanted: list):
    for products in permutations(wanted, r=3):
        print(' '.join(products))


def main():
    n = int(input())
    wanted = [input().split(', ') for _ in range(n)]
    wanted = chain.from_iterable(wanted)
    solution(sorted(wanted))


if __name__ == '__main__':
    main()
