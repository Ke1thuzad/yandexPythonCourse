def solution(val: str):
    mx = 0
    for i in val:
        if int(i) > mx:
            mx = int(i)

    return mx


def main():
    val = input()
    print(solution(val))


if __name__ == '__main__':
    main()
