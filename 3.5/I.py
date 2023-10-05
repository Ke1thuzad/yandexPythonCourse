def solution(first_file_title: str, answer_file_title: str):
    res = ''
    with open(first_file_title, encoding='UTF-8') as f:
        inp = f.read().replace('\t', '').strip(' ').rstrip(' ') + ' '
    for i in range(len(inp) - 1):
        if not((inp[i] == ' ' and inp[i + 1] == ' ') or (inp[i] == '\n' and inp[i + 1] == '\n')):
            res += inp[i]
    with open(answer_file_title, 'w', encoding='UTF-8') as f:
        f.write(res)


def main():
    first_file_title = input()
    answer_file_title = input()
    solution(first_file_title, answer_file_title)


if __name__ == '__main__':
    main()
