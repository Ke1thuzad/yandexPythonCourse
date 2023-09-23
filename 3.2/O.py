def solution(vals: list[int]):
    result = []
    for value in vals:
        binary_val = bin(value)[2:]
        digits = len(binary_val)
        units = binary_val.count('1')
        zeros = digits - units
        result.append({'digits': digits, 'units': units, 'zeros': zeros})
    print(result)


def main():
    vals = list(map(int, input().split()))
    solution(vals)


if __name__ == '__main__':
    main()
