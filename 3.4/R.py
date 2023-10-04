from itertools import product


def solution(expression: str):
    print('a b c f')
    for a, b, c in product(range(2), repeat=3):
        f = int(eval(expression))
        print(a, b, c, f)


def main():
    expression = input()
    solution(expression)


if __name__ == '__main__':
    main()
