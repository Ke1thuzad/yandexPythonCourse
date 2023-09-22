def solution(number: int):
    fst = number // 100
    snd = number // 10 % 10
    lst = number % 10
    mx = 0
    md = 0
    mn = 0

    if fst > snd and fst > lst:
        mx = fst
        if snd > lst:
            md = snd
            mn = lst
        else:
            md = lst
            mn = snd
    elif snd > fst and snd > lst:
        mx = snd
        if fst > lst:
            md = fst
            mn = lst
        else:
            md = lst
            mn = fst
    elif fst > snd:
        mx = lst
        md = fst
        mn = snd
    else:
        mx = lst
        md = snd
        mn = fst
        
    if (mx + mn) == md * 2:
        print('YES')
    else:
        print('NO')


def main():
    number = int(input())
    solution(number)


if __name__ == '__main__':
    main()
