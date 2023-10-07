from math import ceil


def solution(total_byte_size: int):
    measures = {'КБ': 2 ** 10, 'МБ': 2 ** 20, 'ГБ': 2 ** 30}
    for title, measure in reversed(measures.items()):
        if total_byte_size / measure >= 1:
            print(f'{ceil(total_byte_size / measure)}{title}')
            break
    else:
        print(f'{total_byte_size}Б')


def main():
    file_name = input()
    with open(file_name, 'rb') as f:
        total_byte_size = len(f.read())
    solution(total_byte_size)


if __name__ == '__main__':
    main()