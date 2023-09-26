from itertools import product


def solution(ignore: str):
    mast = ['пик', 'треф', 'бубен', 'червей']
    mast.remove(ignore)
    specials = ['валет', 'дама', 'король', 'туз']
    nums = [str(i) for i in range(2, 11)]
    combs = product(nums + specials, mast)
    print('\n'.join(' '.join(comb) for comb in combs))


def main():
    ignore = input()
    solution(ignore)


if __name__ == '__main__':
    main()
