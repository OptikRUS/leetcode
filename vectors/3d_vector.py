from point import Point3D


class Vector3D(Point3D):

    def __init__(self, x, y, z=None):
        if isinstance(x, tuple) and isinstance(y, tuple):
            self.x = y[0] - x[0]
            self.y = y[1] - x[1]
            self.z = y[2] - x[2]
        else:
            super().__init__(x, y, z)

    def vector_mul(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.x * other.z - self.z * other.x
        z = self.x * other.y - self.y * other.x
        return x, y, z

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __mul__(self, num):
        self.x *= num
        self.y *= num
        self.z *= num

    def __add__(self, other):
        return self.x + other.x, self.y + other.y, self.z + other.z

    def __sub__(self, other):
        return self.x - other.x, self.y - other.y, self.z - other.z
