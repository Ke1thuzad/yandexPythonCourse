def solution(values: list):
    last_nod = find_nod(values[0], values[1])
    for i in range(2, len(values)):
        last_nod = find_nod(last_nod, values[i])
    print(last_nod)


def find_nod(a: int, b: int):
    remainder = a % b
    while remainder != 0:
        a, b = b, remainder
        remainder = a % b
    return b


def main():
    n = int(input())
    values = []
    for i in range(n):
        values.append(int(input()))
    solution(values)


if __name__ == '__main__':
    main()
