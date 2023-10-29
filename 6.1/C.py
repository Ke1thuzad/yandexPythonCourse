import math


def solution(n: int, m: int):
    total_variations = math.comb(n, m)
    good_variations = (m * total_variations) // n
    print(good_variations, total_variations)


def main():
    n, m = map(int, input().split())
    solution(n, m)


if __name__ == '__main__':
    main()
