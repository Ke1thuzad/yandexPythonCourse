def solution(n: int):
    total = 0
    for i in range(n):
        value = input()
        for digit in value:
            total += int(digit)
    print(total)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
