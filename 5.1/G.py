def sign(x: int):
    return -1 if x < 0 else 1


class Rectangle:
    def __init__(self, angles1, angles2):
        self.side_coords = []
        self.x1 = angles1[0]
        self.x2 = angles2[0]
        self.y1 = angles1[1]
        self.y2 = angles2[1]
        self.a, self.b = 0, 0
        # top left - 0, top right - 1, bot right - 2, bot left - 3
        self.generate_sides()
        self.compute_wh()

    def generate_sides(self):
        self.side_coords = [[min(self.x1, self.x2), max(self.y1, self.y2)],
                            [max(self.x1, self.x2), max(self.y1, self.y2)],
                            [max(self.x1, self.x2), min(self.y1, self.y2)],
                            [min(self.x1, self.x2), min(self.y1, self.y2)]]

    def compute_wh(self):
        self.a = abs(self.x1 - self.x2)
        self.b = abs(self.y1 - self.y2)

    def perimeter(self):
        return round((self.a + self.b) * 2, 2)

    def area(self):
        return round(self.a * self.b, 2)

    def get_pos(self):
        return tuple(round(i, 2) for i in self.side_coords[0])

    def get_size(self):
        return round(self.a, 2), round(self.b, 2)

    def move(self, dx, dy):
        for i in range(len(self.side_coords)):
            x, y = self.side_coords[i]
            self.side_coords[i] = [x + dx, y + dy]

    def resize(self, width, height):
        bot_r_x, bot_r_y = self.side_coords[2]
        new_height = self.b - height
        new_width = self.a - width
        self.side_coords[2] = [bot_r_x + new_width * sign(bot_r_x), bot_r_y + new_height * sign(bot_r_y)]
        self.side_coords[3][1] += new_height * sign(self.side_coords[3][1])
        self.side_coords[1][0] += new_width * sign(self.side_coords[1][0])
        self.a = width
        self.b = height

    def turn(self):
        self.x1, self.x2, self.y1, self.y2 = self.y1, self.y2, self.x1, self.x2
        self.generate_sides()
        self.compute_wh()

    def scale(self, times):
        self.x1 *= times
        self.x2 *= times
        self.y1 *= times
        self.y2 *= times
        self.generate_sides()
        self.compute_wh()
