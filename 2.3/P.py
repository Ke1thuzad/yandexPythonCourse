def solution(a: str):
    if a == a[::-1]:
        print('YES')
    else:
        print('NO')


def main():
    a = input()
    solution(a)


if __name__ == '__main__':
    main()
