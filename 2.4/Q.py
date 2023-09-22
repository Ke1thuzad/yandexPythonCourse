def solution(n: int):
    total = 0
    for i in range(n):
        user_input = input()
        total += is_palindrome(user_input)
    print(total)


def is_palindrome(val: str):
    if val == val[::-1]:
        return 1
    return 0


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
