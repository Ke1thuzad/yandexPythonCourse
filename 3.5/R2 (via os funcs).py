from math import ceil
from os.path import getsize


def solution(file_name: str):
    total_byte_size = getsize(file_name)
    measures = {'КБ': 2 ** 10, 'МБ': 2 ** 20, 'ГБ': 2 ** 30}
    for title, measure in reversed(measures.items()):
        if total_byte_size / measure >= 1:
            print(f'{ceil(total_byte_size / measure)}{title}')
            break
    else:
        print(f'{total_byte_size}Б')


def main():
    file_name = input()
    solution(file_name)


if __name__ == '__main__':
    main()
