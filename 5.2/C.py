class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_shift, y_shift):
        self.x += x_shift
        self.y += y_shift

    def length(self, target):
        return round(((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if not args:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(*args[0])
        else:
            super().__init__(*args)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'

    def __add__(self, other):
        return PatchedPoint(self.x + other[0], self.y + other[1])

    def __iadd__(self, other):
        self.x += other[0]
        self.y += other[1]
        return self


point = PatchedPoint()
print(point)
new_point = point + (2, -3)
print(point, new_point, point is new_point)
