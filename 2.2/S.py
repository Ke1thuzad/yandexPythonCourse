def solution(x: float, y:float):
    dangerzone_conditions = [(y >= (0.25 * x ** 2) + 0.5 * x - (35 / 4)) and y < 0,
                             ((x ** 2 + y ** 2) <= 25) and (x >= 0) and (y >= 0),
                             (y <= 5) and (x >= -4) and (x < 0) and (y > 0),
                             (y <= (5 / 3) * x + (35 / 3)) and (y > 0) and (x < -4)]
    if x ** 2 + y ** 2 > 100:
        print('Вы вышли в море и рискуете быть съеденным акулой!')
    elif any(dangerzone_conditions):
        print('Опасность! Покиньте зону как можно скорее!')
    else:
        print('Зона безопасна. Продолжайте работу.')


def main():
    x_coord = float(input())
    y_coord = float(input())
    solution(x_coord, y_coord)


if __name__ == '__main__':
    main()
