def solution(a: str):
    mx = 0
    md = 0
    mn = 0
    for i in a:
        b = int(i)
        if b > mx:
            md, mx, mn = mx, b, md
        elif b > md:
            md, mn = b, md
        else:
            mn = b
    mx, md, mn = map(str, (mx, md, mn))
    if mn != '0':
        print(mn + md, mx + md)
    else:
        print(md + mn, mx + md)


def main():
    a = input()
    solution(a)


if __name__ == '__main__':
    main()
