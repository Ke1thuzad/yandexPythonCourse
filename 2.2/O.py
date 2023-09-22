def solution(a: str, b: str):
    all_nums = []
    for i in range(2):
        all_nums.append(int(a[i]))
        all_nums.append(int(b[i]))
    mx = max(all_nums)
    mn = min(all_nums)
    all_nums.remove(mx)
    all_nums.remove(mn)
    print(str(mx) + str(sum(all_nums))[-1] + str(mn))


def main():
    a = input()
    b = input()
    solution(a, b)


if __name__ == '__main__':
    main()
