def solution(n: int, m: int):
    ovs = set()
    mannaya = set()
    for i in range(n + m):
        if i % 2 != 0:
            ovs.add(input())
        else:
            mannaya.add(input())
    intersect = mannaya.symmetric_difference(ovs)
    if intersect:
        print(len(intersect))
    else:
        print('Таких нет')


def main():
    n = int(input())
    m = int(input())
    solution(n, m)


if __name__ == '__main__':
    main()
