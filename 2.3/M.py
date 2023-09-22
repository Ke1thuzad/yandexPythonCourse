def solution():
    n = int(input())
    mn = 10e6
    mname = ''
    for i in range(n):
        a = input()
        acode = ord(a[0])
        if acode < mn:
            mn = acode
            mname = a
        elif acode == mn and ord(a[1]) < ord(mname[1]):
            mn = acode
            mname = a
    print(mname)


def main():
    solution()


if __name__ == '__main__':
    main()
