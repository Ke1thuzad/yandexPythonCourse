def solution(a: int, b: int):
    remainder = a % b
    while remainder != 0:
        a, b = b, remainder
        remainder = a % b
    print(b)


def main():
    a = int(input())
    b = int(input())
    solution(a, b)


if __name__ == '__main__':
    main()
