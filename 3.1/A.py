def solution(n: int):
    good_letters = ['а', 'б', 'в']
    for i in range(n):
        word = input()
        if word[0] not in good_letters:
            print('NO')
            break
    else:
        print('YES')


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
