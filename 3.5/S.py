def solution(shift: int):
    shift = (shift + 26) % 26
    with open('public.txt', encoding='UTF-8') as f:
        str_to_encrypt = f.read().rstrip('\n')
    out = ''
    for letter in str_to_encrypt:
        if letter.isalpha():
            next_letter_code = max((65 + (ord(letter.upper()) + shift) % 91) % 91, (ord(letter.upper()) + shift) % 91)
            if letter.islower():
                next_letter_code += 32
            out += chr(next_letter_code)
        else:
            out += letter
    with open('private.txt', 'w', encoding='UTF-8') as f:
        f.write(out)


def main():
    shift = int(input())
    solution(shift)


if __name__ == '__main__':
    main()
