import math


def solution(x: float):
    formula = ((3 / 16) * math.log(x, 32) + math.pow(x, math.cos((math.pi * x) / (2 * math.e))) -
               math.pow(math.sin(x / math.pi), 2))
    print(formula)


def main():
    x = float(input())
    solution(x)


if __name__ == '__main__':
    main()
