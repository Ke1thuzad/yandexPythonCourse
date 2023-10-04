from itertools import product


def solution(expression: str):
    expression = expression.replace('->', '<')
    expression = expression.replace('~', '=')
    expression = expression.replace('and', '&')
    expression = expression.replace('or', '|')
    expression = expression.replace('not', '!')
    expression = expression.replace('(', ' ( ')
    expression = expression.replace(')', ' ) ')
    uniques = sorted({i for i in expression if i.isupper()})
    print(' '.join(uniques) + ' F')
    for variables in product(range(2), repeat=len(uniques)):
        expr_mas = expression.split()
        locs = dict(zip(uniques, variables))
        f = define_operation(expr_mas, locs)
        print(f"{' '.join(map(str, variables))} {f}")


def define_operation(expr_mas: list, locs: dict):
    while '(' in expr_mas and ')' in expr_mas:
        bracket_id = expr_mas.index('(') + 1
        closing_bracket_id = expr_mas.index(')', bracket_id) + 1
        if '(' in expr_mas[bracket_id:closing_bracket_id]:
            double_bracket_id = expr_mas.index('(', bracket_id, closing_bracket_id)
            expr_mas[double_bracket_id:closing_bracket_id] = \
                [define_operation(expr_mas[double_bracket_id + 1:closing_bracket_id], locs)]
            closing_bracket_id = expr_mas.index(')', bracket_id) + 1

        expr_mas[bracket_id - 1:closing_bracket_id] = \
            [define_operation(expr_mas[bracket_id:closing_bracket_id], locs)]

    while '!' in expr_mas:
        not_id = expr_mas.index('!')
        next_val = expr_mas[not_id + 1]
        expr_mas[not_id:not_id + 2] = [int(eval(f'not {next_val}', locs))]

    while '&' in expr_mas:
        and_id = expr_mas.index('&')
        expr_mas[and_id - 1:and_id + 2] = \
            [eval_operation(expr_mas[and_id - 1:and_id + 2], locs)]

    while '^' in expr_mas:
        xor_id = expr_mas.index('^')
        expr_mas[xor_id - 1:xor_id + 2] = \
            [eval_operation(expr_mas[xor_id - 1:xor_id + 2], locs)]

    while '|' in expr_mas:
        or_id = expr_mas.index('|')
        expr_mas[or_id - 1:or_id + 2] = \
            [eval_operation(expr_mas[or_id - 1:or_id + 2], locs)]

    while '<' in expr_mas:
        implic_id = expr_mas.index('<')
        expr_mas[implic_id - 1:implic_id + 2] = \
            [eval_operation(expr_mas[implic_id - 1:implic_id + 2], locs)]

    while '=' in expr_mas:
        equality_id = expr_mas.index('=')
        expr_mas[equality_id - 1:equality_id + 2] = \
            [eval_operation(expr_mas[equality_id - 1:equality_id + 2], locs)]

    return expr_mas[0]


def eval_operation(cur_operation: list, variables: dict):
    operation = list(map(str, cur_operation))
    variables.update({'1': 1, '0': 0})
    val1, oper, val2 = operation
    match oper:
        case '<':
            return int(variables[val1] <= variables[val2])
        case '=':
            return int(variables[val1] == variables[val2])
        case _:
            return eval(''.join(operation), variables)


def main():
    inp_expression = input()
    solution(inp_expression)


if __name__ == '__main__':
    main()
