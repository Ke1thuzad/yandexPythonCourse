def solution(n: int):
    count = 0
    for i in range(n):
        sentence = input()
        if 'зайка' in sentence:
            count += 1
    print(count)


def main():
    n = int(input())
    solution(n)


if __name__ == '__main__':
    main()
