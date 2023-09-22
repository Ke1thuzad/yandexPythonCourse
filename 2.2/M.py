def solution(a, b, c):
    if a[0] in b and a[0] in c:
        print(a[0])
    else:
        print(a[1])


def main():
    a = input()
    b = input()
    c = input()
    solution(a, b, c)


if __name__ == '__main__':
    main()
