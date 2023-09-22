def solution(values: list[str]):
    stack = []
    i = 0
    while i < len(values):
        cur_val = values[i]
        if cur_val.isnumeric():
            stack.append(cur_val)
        else:
            calculate_via_operator(values[i], stack)
        i += 1
    print(stack[0])


def calculate_via_operator(operator: str, stack: list):
    binary_opers = ['+', '-', '*', '/']

    if operator in binary_opers:
        last_val = stack.pop()
        prelast_val = stack.pop()
        if operator == '/':
            operator += '/'
        result = eval(prelast_val + operator + last_val)
        stack.append(str(result))
    elif operator == '~':
        stack[-1] = "-" + stack[-1]
    elif operator == '!':
        stack[-1] = factorial(int(stack[-1]))
    elif operator == '#':
        stack.append(stack[-1])
    elif operator == '@':
        stack.append(stack.pop(-3))
    return stack


def factorial(n: int):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


def main():
    values = input().split()
    solution(values)


if __name__ == '__main__':
    main()
