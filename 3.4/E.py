def solution(products: list):
    for i, product in enumerate(sorted(products), 1):
        print(f'{i}. {product}'.strip(','))


def main():
    a = input().split()
    b = input().split()
    c = input().split()
    solution(a + b + c)


if __name__ == '__main__':
    main()
