def solution(info: str):
    for digit in info:
        # getting last 8 bytes using bitwise conjunction and converting to a new symbol
        print(chr(ord(digit) & 255), end='')


def main():
    with open('secret.txt', encoding='UTF-8') as f:
        info = f.read().rstrip('\n')
    solution(info)


if __name__ == '__main__':
    main()
