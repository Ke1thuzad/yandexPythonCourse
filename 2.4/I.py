def solution(n: int):
    result = ''
    for i in range(n):
        mx = 0
        val = input()
        for digit in val:
            mx = max(mx, int(digit))
        result += str(mx)
    print(result)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
