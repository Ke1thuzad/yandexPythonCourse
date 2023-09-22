def generate_christmas_tree(limit: int):
    tree = []
    row = []
    n = 1
    row_index = 1
    elems_in_row = 0
    while n <= limit:
        row.append(n)
        elems_in_row += 1
        n += 1
        if elems_in_row == row_index:
            tree.append(row)
            row = []
            elems_in_row = 0
            row_index += 1
    if row:
        tree.append(row)
    return tree


def count_max_len(branch: list):
    letters = 0
    spaces = 0
    for val in branch:
        letters += len(str(val))
    spaces = len(branch) - 1
    total = letters + spaces
    return total


def solution(n: int):
    christmas_tree = generate_christmas_tree(n)
    max_len = count_max_len(max(christmas_tree))
    for i in range(len(christmas_tree)):
        out = ''
        for j in range(len(christmas_tree[i])):
            out += str(christmas_tree[i][j]) + ' '

        out = out[:-1]
        print(f'{out: ^{max_len}}')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
