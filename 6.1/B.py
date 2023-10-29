import math
from sys import stdin


def main():
    for sequence in stdin:
        vals = map(int, sequence.split())
        print(math.gcd(*vals))


if __name__ == '__main__':
    main()
