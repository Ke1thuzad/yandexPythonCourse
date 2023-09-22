def solution(limit: int):
    n = 1
    row = 1
    elems_in_row = 0
    while n <= limit:
        print(n, end=' ')
        elems_in_row += 1
        n += 1
        if elems_in_row == row:
            print()
            elems_in_row = 0
            row += 1


def main():
    limit = int(input())
    solution(limit)


if __name__ == '__main__':
    main()
