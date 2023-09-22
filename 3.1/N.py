def solution(values: list[int], p: int):
    print(*[val ** p for val in values], sep=' ')


def main():
    values = list(map(int, input().split()))
    p = int(input())
    solution(values, p)


if __name__ == '__main__':
    main()
