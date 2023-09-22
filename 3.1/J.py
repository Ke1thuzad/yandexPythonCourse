def solution(sentences: list[str]):
    print(max(count_unique_letters(''.join(sentences).lower().replace(' ', '')).items(), key=lambda x: x[1])[0])


def count_unique_letters(x: str):
    result = {}
    for letter in x:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result


def main():
    sentence = input()
    sentences = []
    while sentence != 'ФИНИШ':
        sentences.append(sentence)
        sentence = input()
    solution(sentences)


if __name__ == '__main__':
    main()
