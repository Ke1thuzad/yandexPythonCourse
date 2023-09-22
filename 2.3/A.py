def solution(word):
    while word != 'Три!':
        print('Режим ожидания...')
        word = input()
    print('Ёлочка, гори!')


def main():
    word = input()
    solution(word)


if __name__ == '__main__':
    main()
