class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # длина вектора
    def length(self):
        return (self.x ** 2 + self.y ** 2) ** 0.5

    # умножение вектора на число
    def mulnum(self, num):
        self.x *= num
        self.y *= num

    def __str__(self):
        return f"coord x: {self.x}, coord y: {self.y}"

    # сложение векторов
    def __add__(self, other):
        return self.x + other.x, self.y + other.y

    # вычитание векторов
    def __sub__(self, other):
        return self.x - other.x, self.y - other.y

    # умножение векторов
    def __mul__(self, other):
        return self.x * other.x + self.y * other.y

    # угол между векторами
    def __truediv__(self, other):
        return (self.x * other.x + self.y * other.y) / (self.length() * other.length())
