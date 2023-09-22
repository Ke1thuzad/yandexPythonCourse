def solution(n: int):
    participants = {}
    for i in range(n):
        student = input()
        val = input()
        participants[digit_sum(val)] = student
    print(sorted(participants.items(), reverse=True)[0][1])


def digit_sum(x: str):
    total = 0
    for digit in x:
        total += int(digit)

    return total


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
