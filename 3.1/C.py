def solution(max_len: int, n: int):
    for i in range(n):
        title = input()
        if len(title) > max_len:
            title = title[:max_len - 3] + '...'
        print(title)


def main():
    max_len = int(input())
    n = int(input())
    solution(max_len, n)


if __name__ == '__main__':
    main()
