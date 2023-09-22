def solution(x: int):
    factors = []
    for i in range(2, x + 1):
        while x % i == 0:
            factors.append(i)
            x //= i
    print(*factors, sep=' * ')


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
