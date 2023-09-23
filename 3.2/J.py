def solution(sentence: str):
    code = {
        "А": "A",
        "Б": "B",
        "В": "V",
        "Г": "G",
        "Д": "D",
        "Е": "E",
        "Ё": "E",
        "Ж": "ZH",
        "З": "Z",
        "И": "I",
        "Й": "I",
        "К": "K",
        "Л": "L",
        "М": "M",
        "Н": "N",
        "О": "O",
        "П": "P",
        "Р": "R",
        "С": "S",
        "Т": "T",
        "У": "U",
        "Ф": "F",
        "Х": "KH",
        "Ц": "TC",
        "Ч": "CH",
        "Ш": "SH",
        "Щ": "SHCH",
        "Ы": "Y",
        "Э": "E",
        "Ю": "IU",
        "Я": "IA",
        "Ь": "",
        "Ъ": "",
    }
    for letter in sentence:
        if letter.isalpha() and letter.upper() in code:
            if letter.isupper():
                print(code[letter.upper()].title(), end="")
            else:
                print(code[letter.upper()].lower(), end="")
        else:
            print(letter, end="")


def main():
    sentence = input()
    solution(sentence)


if __name__ == "__main__":
    main()
