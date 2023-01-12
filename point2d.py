class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Точка({self.x}, {self.y})'


class Point3D(Point2D):
    def __init__(self, x, y, z):
        super().__init__(x, y)
        self.z = z

    def __str__(self):
        return f'Точка({self.x}, {self.y}, {self.z})'


point1 = Point2D(1, 2)
point2 = Point3D(1, 2, 3)
print(point1)
print(point2)
