def solution(n: int):
    for i in range(n):
        sentence = input()
        if 'зайка' in sentence:
            print(sentence.find('зайка') + 1)
        else:
            print('Заек нет =(')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
