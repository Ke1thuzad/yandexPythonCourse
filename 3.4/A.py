def solution(words: list):
    for i, word in enumerate(words, 1):
        print(f'{i}. {word}')


def main():
    words = input().split()
    solution(words)


if __name__ == '__main__':
    main()
