def solution(n: int, m: int):
    last_val = 1
    last_row_val = 1
    max_len = len(str(n * m))
    for i in range(n):
        last_val = last_row_val
        for j in range(m):
            print(f'{last_val: >{max_len}}', end=' ')
            last_val += n
        last_row_val += 1
        print()


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
