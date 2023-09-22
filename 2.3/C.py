def solution(rangestart: int, rangestop: int):
    print(*[i for i in range(rangestart, rangestop + 1)], sep=' ')


def main():
    rangestart, rangestop = int(input()), int(input())
    solution(rangestart, rangestop)


if __name__ == '__main__':
    main()
