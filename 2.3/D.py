def solution(rangestart: int, rangestop: int):
    rangestep = 1
    if rangestart > rangestop:
        rangestep = -1
        rangestop -= 1
    else:
        rangestop += 1
    print(*[i for i in range(rangestart, rangestop, rangestep)], sep=' ')


def main():
    rangestart, rangestop = int(input()), int(input())
    solution(rangestart, rangestop)


if __name__ == '__main__':
    main()
