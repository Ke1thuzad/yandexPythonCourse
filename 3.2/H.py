def solution(students: dict, porridge_type: str):
    if porridge_type in students:
        print(*sorted(students[porridge_type]), sep='\n')
    else:
        print('Таких нет')


def main():
    n = int(input())
    students = {}
    for i in range(n):
        name, *porridges = input().split()
        for porridge in porridges:
            if porridge in students:
                students[porridge].append(name)
            else:
                students[porridge] = [name]
    porridge_type = input()
    solution(students, porridge_type)


if __name__ == '__main__':
    main()
