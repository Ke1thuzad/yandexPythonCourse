def solution(a: int, b: int, c: int):
    mx = max(a, b, c)
    mn = min(a, b, c)
    md = [a, b, c]
    md.remove(mx)
    md.remove(mn)
    md = md[0]
    # Cos theorem: a^2 = b^2 + c^2 - 2bc*cosA
    # cosA = (a^2 - b^2 - c^2) / 2bc
    cosmx = (mx ** 2 - md ** 2 - mn ** 2) / (2 * md * mn)
    if cosmx == 0:
        print('100%')
    elif cosmx < 0:
        print('крайне мала')
    else:
        print('велика')



def main():
    a = int(input())
    b = int(input())
    c = int(input())
    solution(a, b, c)


if __name__ == '__main__':
    main()
