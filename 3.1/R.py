def solution(a: str):
    temp = [None, None]
    a += ' '
    for i in range(len(a)):
        if a[i] != temp[0]:
            if i != 0:
                print(*temp)
            temp = [a[i], 1]
        else:
            temp[1] += 1


def main():
    a = input()
    solution(a)


if __name__ == '__main__':
    main()
