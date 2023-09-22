def solution(n: int):
    if n <= 1:
        return 1
    return n * solution(n - 1)


def main():
    n = int(input())
    print(solution(n))


if __name__ == '__main__':
    main()
