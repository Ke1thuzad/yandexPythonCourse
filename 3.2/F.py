def solution(n: int, m: int):
    ovs = set()
    mannaya = set()
    for i in range(n + m):
        inp = input()
        if (i % 2 != 0 and len(ovs) < m) or len(mannaya) >= n:
            if inp in ovs:
                mannaya.add(inp)
            else:
                ovs.add(inp)
        else:
            if inp in mannaya:
                ovs.add(inp)
            else:
                mannaya.add(inp)
    intersect = ovs.symmetric_difference(mannaya)
    if intersect:
        print(*sorted(intersect), sep='\n')
    else:
        print('Таких нет')


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
#2 5 ['PERyPApOZv', 'PERyPApOZv', 'cChzISsAVW'] ['cChzISsAVW', 'ntdRhrTQj', 'UBnzvI', 'jCesRC'] ['PERyPApOZv', 'UBnzvI', 'jCesRC', 'ntdRhrTQj']