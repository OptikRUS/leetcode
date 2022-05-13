class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def corner(self, other):
        return (self.x * other.x + self.y * other.y) / (abs(self) * abs(other))

    def scalar_mul(self, other):
        return self.x * other.x + self.y * other.y

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    def __mul__(self, num):
        self.x *= num
        self.y *= num

    def __str__(self):
        return f"coord x: {self.x}, coord y: {self.y}"

    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y
