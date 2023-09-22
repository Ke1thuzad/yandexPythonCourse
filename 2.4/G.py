def solution(n: int):
    for i in range(n):
        for j in range(3 + i, 0, -1):
            print('До старта ' + str(j) + ' секунд(ы)')
        print(f'Старт {i + 1}!!!')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
