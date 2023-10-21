class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x_shift, y_shift):
        self.x += x_shift
        self.y += y_shift

    def length(self, target):
        return round(((self.x - target.x) ** 2 + (self.y - target.y) ** 2) ** 0.5, 2)
