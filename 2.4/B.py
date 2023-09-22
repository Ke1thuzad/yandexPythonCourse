def solution(size: int):
    for i in range(1, size + 1):
        for j in range(1, size + 1):
            print(f'{j} * {i} = {i * j}')


def main():
    size = int(input())
    solution(size)


if __name__ == '__main__':
    main()
