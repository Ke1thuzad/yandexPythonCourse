from sys import stdin


def solution():
    total = 0
    for inp in stdin:
        total += sum(map(int, inp.split()))
    print(total)


def main():
    solution()


if __name__ == '__main__':
    main()
