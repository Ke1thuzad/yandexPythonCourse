def solution(values: list[str]):
    stack = []
    i = 0
    while i < len(values):
        cur_val = values[i]
        if cur_val.isnumeric():
            stack.append(cur_val)
        else:
            last_val = stack.pop(-1)
            prelast_val = stack.pop(-1)
            result = eval(prelast_val + values[i] + last_val)
            stack.append(str(result))

        i += 1
    print(stack[0])


def main():
    values = input().split()
    solution(values)


if __name__ == '__main__':
    main()
