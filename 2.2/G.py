def solution(num: str):
    if num == num[::-1]:
        print('YES')
    else:
        print('NO')


def main():
    num = input()
    solution(num)


if __name__ == '__main__':
    main()
