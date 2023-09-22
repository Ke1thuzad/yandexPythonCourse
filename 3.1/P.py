def solution(n: int, max_len: int):

    used_symbols = 0
    for i in range(n):
        title = input()
        if len(title) + used_symbols + 3 >= max_len:
            print(title[:max_len - used_symbols - 3] + '...')
            break
        else:
            print(title)
        used_symbols += len(title)


def main():
    max_len = int(input())
    n = int(input())

    solution(n, max_len)


if __name__ == '__main__':
    main()
