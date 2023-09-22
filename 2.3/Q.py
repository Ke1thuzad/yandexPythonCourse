def solution(a: str):
    result = ''
    for w in a:
        if int(w) % 2 != 0:
            result += w
    print(result)


def main():
    a = input()
    solution(a)


if __name__ == '__main__':
    main()
