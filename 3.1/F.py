def solution(n: int):
    total = 0
    for i in range(n):
        sentence = input()
        total += sentence.count('зайка')
    print(total)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
