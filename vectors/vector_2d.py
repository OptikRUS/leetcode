from vectors.point import Point


class Vector(Point):

    def __init__(self, x, y):
        if isinstance(x, tuple) and isinstance(y, tuple):
            self.x = float(y[0] - x[0])
            self.y = float(y[1] - x[1])
        elif isinstance(x, Point) and isinstance(y, Point):
            self.x = y.x - x.x
            self.y = y.y - x.y
        elif isinstance(x, Point) and isinstance(y, tuple):
            self.x = y[0] - x.x
            self.y = y[1] - x.y
        elif isinstance(x, tuple) and isinstance(y, Point):
            self.x = y.x - x[0]
            self.y = y.y - x[1]
        else:
            super().__init__(x, y)

    def corner(self, other):
        return (self.x * other.x + self.y * other.y) / (abs(self) * abs(other))

    def scalar_mul(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __mul__(self, num):
        self.x *= num
        self.y *= num

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)
