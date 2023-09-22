def solution(a):
    ml = a % 10 + (a // 10) % 10
    st = a // 100 + (a // 10) % 10
    print(''.join(map(str, sorted((ml, st), reverse=True))))


def main():
    a = int(input())
    solution(a)


if __name__ == '__main__':
    main()
