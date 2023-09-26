from itertools import count


def solution(start: float, stop: float, step: float):
    for num in count(start, step):
        if num >= stop:
            break
        print(f'{num:.2f}')


def main():
    start, stop, step = map(float, input().split())
    solution(start, stop, step)


if __name__ == '__main__':
    main()
