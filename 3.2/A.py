def solution(a: str):
    print(*set(a), sep='')


def main():
    a = input()
    solution(a)


if __name__ == '__main__':
    main()
