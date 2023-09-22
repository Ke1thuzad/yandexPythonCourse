def solution(n: int):
    result = 0
    for j in range(n):
        result += is_prime(int(input()))
    print(result)


def is_prime(x: int):
    if x == 1: return 0
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return 0
    return 1


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
