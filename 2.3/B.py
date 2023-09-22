def solution(sentences: list):
    count = 0
    for i in sentences:
        if 'зайка' in i:
            count += 1
    print(count)


def main():
    sentences = []
    sentence = input()
    while sentence != 'Приехали!':
        sentences.append(sentence)
        sentence = input()
    solution(sentences)


if __name__ == '__main__':
    main()
