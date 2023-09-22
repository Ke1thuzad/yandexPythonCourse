def solution(a: int, b: int, c: int):
    mx = max(a, b, c)
    mn = min(a, b, c)
    md = [a, b, c]
    md.remove(mx)
    md.remove(mn)
    if mx < (mn + md[0]):
        print('YES')
    else:
        print('NO')


def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
