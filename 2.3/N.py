def solution(x: int):
    if x == 1:
        print('NO')
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                print('NO')
                break
        else:
            print('YES')


def main():
    x = int(input())
    solution(x)


if __name__ == '__main__':
    main()
