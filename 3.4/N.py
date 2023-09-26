from itertools import permutations


def solution(sportsmen: list):
    for start in permutations(sportsmen, r=3):
        print(', '.join(start))


def main():
    n = int(input())
    sportsmen = [input() for _ in range(n)]
    solution(sorted(sportsmen))


if __name__ == '__main__':
    main()
