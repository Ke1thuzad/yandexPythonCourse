def solution(p: int, v: int):
    p += 6
    v += 12

    if p > v:
        print('Петя')
    else:
        print('Вася')


def main():
    p = int(input())
    v = int(input())
    solution(p, v)


if __name__ == '__main__':
    main()
