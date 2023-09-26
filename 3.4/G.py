from itertools import combinations


def solution(participants: list):
    for i in combinations(participants, r=2):
        print(' - '.join(i))


def main():
    n = int(input())
    participants = []
    for i in range(n):
        participants.append(input())
    solution(participants)


if __name__ == '__main__':
    main()
