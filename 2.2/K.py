def solution(number: str):
    digits = list(map(int, number))
    mx = max(digits)
    mn = min(digits)
    digits.remove(mx)
    digits.remove(mn)
    md = digits[0]
    
        
    if (mx + mn) == md * 2:
        print('YES')
    else:
        print('NO')


def main():
    number = input()
    solution(number)


if __name__ == '__main__':
    main()

