def solution(a: str, b: str):
    print(*(set(a).intersection(set(b))), sep='')


def main():
    a = input()
    b = input()
    solution(a, b)


if __name__ == '__main__':
    main()
