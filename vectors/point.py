class Point:
    def __init__(self, x, y):
        try:
            self.x = float(x)
            self.y = float(y)
        except (ValueError, TypeError) as error:
            raise error

    def __str__(self):
        return f"coord x: {self.x} coord y: {self.y}"


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        try:
            self.z = float(z)
        except (ValueError, TypeError) as error:
            raise error

    def __str__(self):
        return f"{super().__str__()} coord z: {self.z}"
