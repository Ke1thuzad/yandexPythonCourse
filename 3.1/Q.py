def solution(sentence: str):
    formatted_sentence = sentence.replace(' ', '').lower()
    if formatted_sentence == formatted_sentence[::-1]:
        print('YES')
    else:
        print('NO')


def main():
    sentence = input()
    solution(sentence)


if __name__ == '__main__':
    main()
