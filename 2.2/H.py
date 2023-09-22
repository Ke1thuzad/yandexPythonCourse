def solution(words):
    for i in range(len(words)):
        if words[i] == 'зайка':
            print('YES')
            break
    else:
        print('NO')


def main():
    sentence = input()
    solution(sentence.split())


if __name__ == '__main__':
    main()
