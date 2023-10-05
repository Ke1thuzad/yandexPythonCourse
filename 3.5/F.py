def solution(sentence: str):
    result = ''
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
                result += code[letter.upper()].title()
            else:
                result += code[letter.upper()].lower()
        else:
            result += letter
    return result


def main():
    with open('cyrillic.txt', 'r', encoding='UTF-8') as f:
        sentence = f.read().rstrip('\n')
    res = solution(sentence)
    with open('transliteration.txt', 'w', encoding='UTF-8') as f:
        f.write(res)


if __name__ == '__main__':
    main()
