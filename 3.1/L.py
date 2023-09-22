def solution(n: int):
    porridges = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
    for i in range(n):
        print(porridges[i % 5])


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
