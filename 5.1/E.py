class Rectangle:
    def __init__(self, angles1, angles2):
        self.left_side = angles1
        self.right_side = angles2
        self.a = abs(self.left_side[0] - self.right_side[0])
        self.b = abs(self.left_side[1] - self.right_side[1])

    def perimeter(self):
        return round((self.a + self.b) * 2, 2)

    def area(self):
        return round(self.a * self.b, 2)
