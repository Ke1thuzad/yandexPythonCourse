from sys import stdin


def solution(deviations: list):
    print(round(sum(deviations) / len(deviations)))


def main():
    deviations = []
    for inp in stdin:
        info = inp.split()
        deviations.append(abs(int(info[2]) - int(info[1])))
    solution(deviations)


if __name__ == '__main__':
    main()
