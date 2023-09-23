def solution(n: int, m: int):
    ovs = set()
    mannaya = set()
    for i in range(n):
        ovs.add(input())
    for j in range(m):
        mannaya.add(input())
    intersect = ovs.intersection(mannaya)
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
