import math


def solution(x, y, ro, fiInRad):
    xp, xy = ro * math.cos(fiInRad), ro * math.sin(fiInRad)
    vector = (x - xp, y - xy)
    vector_magnitude = math.sqrt((vector[0] ** 2 + vector[1] ** 2))
    print(vector_magnitude)


def main():
    x, y = map(float, input().split())
    ro, fiInRad = map(float, input().split())
    solution(x, y, ro, fiInRad)


if __name__ == '__main__':
    main()
