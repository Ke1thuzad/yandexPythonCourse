def solution(n: int):
    uniques = {}
    for i in range(n):
        surname = input()
        if surname in uniques:
            uniques[surname] += 1
        else:
            uniques[surname] = 1
    some_uniques = 0
    for last_name, count in uniques.items():
        if count > 1:
            print(f'{last_name} - {count}')
            some_uniques = 1
    if not some_uniques:
        print('Однофамильцев нет')



def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
