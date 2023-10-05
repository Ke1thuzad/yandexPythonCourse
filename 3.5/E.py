from sys import stdin


def find_palindromes(sentence: list):
    palindromes = []
    for word in sentence:
        if word.lower() == word[::-1].lower():
            palindromes.append(word)
    return palindromes


def main():
    pals = set()
    for sentence in stdin:
        pals.update(find_palindromes(sentence.split()))
    print(*sorted(pals), sep='\n')


if __name__ == '__main__':
    main()
