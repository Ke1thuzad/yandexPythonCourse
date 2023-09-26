from itertools import product


def solution(expression: str):
    expression = expression.replace("->", "<=")
    expression = expression.replace("~", "==")
    uniques = sorted({i for i in expression if i.isupper()})
    print(" ".join(uniques) + " F")
    for variables in product(range(2), repeat=len(uniques)):
        locs = dict(zip(uniques, variables))
        f = int(eval(expression, locs))
        print(f"{' '.join(map(str, variables))} {f}")


def main():
    expression = input()
    solution(expression)


if __name__ == "__main__":
    main()
