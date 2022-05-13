from vectors.point import Point3D


class Vector3D(Point3D):

    def __init__(self, x, y, z):
        if isinstance(x, tuple) and isinstance(y, tuple) and isinstance(z, tuple):
            self.x = float(y[0] - x[0])
            self.y = float(y[1] - x[1])
            self.z = float(y[2] - x[2])
        elif isinstance(x, Point3D) or isinstance(y, Point3D) or isinstance(y, Point3D):
            self.x = y.x - x.x
            self.y = y.y - x.y
            self.z = y.z - x.z
        else:
            super().__init__(x, y, z)

    def vector_mul(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.x * other.z - self.z * other.x
        z = self.x * other.y - self.y * other.x
        return Vector3D(x, y, z)

    def __abs__(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def __mul__(self, num):
        self.x *= num
        self.y *= num
        self.z *= num

    def __add__(self, other):
        return Vector3D(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector3D(self.x - other.x, self.y - other.y, self.z - other.z)


p1 = Vector3D(1, 2, 3)
p2 = Vector3D(4, 5, 6)
p3 = Vector3D(1, 2, 3)

print(p2.vector_mul(p3))