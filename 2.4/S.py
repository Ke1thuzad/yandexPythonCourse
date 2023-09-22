def solution(size: int):
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            dist = min(i, j, size - i + 1, size - j + 1)
            print(f'{dist: >{len(str(size // 2 + size % 2))}}', end=' ')
        print()


def main():
    size = int(input())
    solution(size)


if __name__ == '__main__':
    main()
