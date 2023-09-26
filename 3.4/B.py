def solution(kids1: list, kids2: list):
    for kid1, kid2 in zip(kids1, kids2):
        print(f'{kid1} - {kid2}'.replace(',', ''))


def main():
    kids1 = input().split()
    kids2 = input().split()
    solution(kids1, kids2)


if __name__ == '__main__':
    main()
