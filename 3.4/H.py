from itertools import cycle, islice


def solution(porridges: list, n: int):
    print('\n'.join(islice(cycle(porridges), n)))


def main():
    m = int(input())
    porridges = [input() for _ in range(m)]
    n = int(input())
    solution(porridges, n)


if __name__ == '__main__':
    main()
