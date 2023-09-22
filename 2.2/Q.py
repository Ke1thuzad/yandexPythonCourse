def solution(a: float, b: float, c: float):
    if not a and not b and not c:
        print('Infinite solutions')
    elif not a and not b and c:
        print('No solution')
    elif not a:
        print(f'{-c / b: .2f}')
    else:
        D = b ** 2 - 4 * a * c
        if D > 0:
            quadric_roots = sorted([(-b - D ** 0.5) / (2 * a), (-b + D ** 0.5) / (2 * a)])
            print(f'{quadric_roots[0]: .2f} {quadric_roots[1]: .2f}')
        elif D == 0:
            print(f'{-b / (2 * a): .2f}')
        else:
            print('No solution')


def main():
    a = float(input())
    b = float(input())
    c = float(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
