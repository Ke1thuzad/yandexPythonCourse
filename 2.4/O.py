def solution(n: int, m: int):
    table = generate_table(n, m)
    max_len = len(str(n * m))
    for i in range(n):
        for j in range(m):
            print(f'{table[j][i]: >{max_len}}', end=' ')
        print()


def generate_table(n: int, m: int):
    last_val = 1
    result = []
    for row_index in range(1, m + 1):
        row = []
        for col in range(n):
            row.append(last_val)
            last_val += 1
        if row_index % 2 == 0:
            row = row[::-1]
        result.append(row)
    return result


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
