def solution(sentences: list):
    rabbit_sentences = []
    for i in range(len(sentences)):
        if 'зайка' in sentences[i]:
            rabbit_sentences.append(sentences[i])
    rabbit_sentences.sort()
    print(rabbit_sentences[0], len(rabbit_sentences[0]))


def main():
    sentences = []
    for _ in range(3):
        sentences.append(input())
    solution(sentences)


if __name__ == '__main__':
    main()
