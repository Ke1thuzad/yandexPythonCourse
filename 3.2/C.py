def solution(n: int):
    uniques = set()
    for i in range(n):
        for obj in input().split():
            uniques.add(obj)
    print(*uniques, sep='\n')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
