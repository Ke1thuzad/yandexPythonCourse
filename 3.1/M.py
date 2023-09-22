def solution(values: list[int], p: int):
    print(*[val ** p for val in values], sep='\n')


def main():
    n = int(input())
    values = []
    for i in range(n):
        values.append(int(input()))
    p = int(input())
    solution(values, p)


if __name__ == '__main__':
    main()
