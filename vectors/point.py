class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self, *args, **kwargs):
        return self.x, self.y

    def __str__(self):
        return f"coord x: {self.x} coord y: {self.y}"


class Point3D(Point):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f"coord x: {self.x} coord y: {self.y} coord z: {self.z}"
