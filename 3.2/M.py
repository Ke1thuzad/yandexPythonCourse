def solution(n: int):
    all_dishes = set()
    done_dishes = set()
    for i in range(n):
        all_dishes.add(input())
    m = int(input())
    for j in range(m):
        for k in range(int(input())):
            done_dishes.add(input())
    not_done_dishes = all_dishes.difference(done_dishes)
    if not_done_dishes:
        print(*sorted(not_done_dishes), sep="\n")
    else:
        print('Готовить нечего')


def main():
    n = int(input())
    solution(n)


if __name__ == "__main__":
    main()
