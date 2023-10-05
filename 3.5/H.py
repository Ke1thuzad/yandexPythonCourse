def solution(first_file_title: str, second_file_title: str, answer_file_title: str):
    words = set()

    with open(first_file_title, encoding='UTF-8') as f:
        words.update(f.read().replace('\n', ' ').split())
    with open(second_file_title, encoding='UTF-8') as f:
        lines = f.read().replace('\n', ' ').split()
        words.symmetric_difference_update(lines)
    with open(answer_file_title, 'w', encoding='UTF-8') as f:
        f.write('\n'.join(sorted(words)))


def main():
    first_file_title = input()
    second_file_title = input()
    answer_file_title = input()
    solution(first_file_title, second_file_title, answer_file_title)


if __name__ == '__main__':
    main()
