from itertools import accumulate


def solution(words: list):
    for sentence in accumulate(words, lambda *x: ' '.join(x)):
        print(sentence)


def main():
    words = input().split()
    solution(words)


if __name__ == '__main__':
    main()
