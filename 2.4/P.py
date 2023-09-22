def solution(size: int, width: int):
    for i in range(1, size + 1):
        for j in range(1, size + 1):

            if j != size:
                print((str(i * j) + " " if width % 2 else str(i * j)).center(width), end='|')
            else:
                print((str(i * j) + " " if width % 2 else str(i * j)).center(width), end='')
        print()
        if i != size:
            print('-' * (size * (width + 1) - 1))


def main():
    size = int(input())
    width = int(input())
    solution(size, width)


if __name__ == '__main__':
    main()
