def solution(vals):
    total = 1
    for val in vals:
        total *= val
    total **= (1 / len(vals))
    print(total)


def main():
    vals = map(float, input().split())
    solution(list(vals))


if __name__ == '__main__':
    main()
