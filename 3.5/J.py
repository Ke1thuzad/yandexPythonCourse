def solution(file_title: str, lim: int):
    with open(file_title, encoding='UTF-8') as f:
        lines = f.readlines()
    print(*lines[-1 * lim:], sep='')


def main():
    file_title = input()
    lim = int(input())
    solution(file_title, lim)


if __name__ == '__main__':
    main()