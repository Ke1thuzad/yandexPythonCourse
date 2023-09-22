def solution(*args, **kwargs):
    total = 0
    cost = float(input())
    while cost != 0:
        if cost >= 500:
            total += cost * 0.9
        else:
            total += cost
        cost = float(input())
    print(total)


def main():
    solution()


if __name__ == '__main__':
    main()
