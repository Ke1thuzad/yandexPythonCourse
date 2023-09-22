def solution(n: int, m: int):
    last_val = 1
    max_len = len(str(n * m))

    for i in range(n):
        for j in range(m):
            print(f'{last_val: >{max_len}}', end=' ')
            if i % 2:
                last_val -= 1
            else:
                last_val += 1
        last_val += m
        if i % 2 != 0:
            last_val += 1
        else:
            last_val -= 1
        print()


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
