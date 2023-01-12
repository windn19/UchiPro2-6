class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __str__(self):
        return f'Прямоугольник со сторонами {self.a} {self.b}'

    def get_area(self):
        return self.a * self.b

class Square(Rectangle):
    def __str__(self):
        return f'Квадрат со стороной {self.a}'

    def get_perimeter(self):
        return self.a * 4


square = Square(5, 5)
rec = Rectangle(5, 6)
print(square.get_perimeter())
print(rec.get_perimeter())