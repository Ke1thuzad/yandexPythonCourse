class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.x += other.x
        self.y += other.y
        return self


def solution(direction, magnitude):
    coords = Vector2(0, 0)
    while 1:
        coords += determine_velocity(direction, magnitude)
        direction = input()
        if direction == 'СТОП':
            break
        magnitude = int(input())
    print(coords.y, coords.x, sep='\n')


def determine_velocity(dir, speed) -> Vector2:
    if dir == 'СЕВЕР':
        velocity = Vector2(0, speed)
    elif dir == 'ВОСТОК':
        velocity = Vector2(speed, 0)
    elif dir == 'ЮГ':
        velocity = Vector2(0, -speed)
    elif dir == 'ЗАПАД':
        velocity = Vector2(-speed, 0)
    else:
        velocity = Vector2(0, 0)

    return velocity


def main():
    direction = input()
    magnitude = int(input())
    solution(direction, magnitude)


if __name__ == '__main__':
    main()
