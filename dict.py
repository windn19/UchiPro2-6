from pprint import pprint


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


pprint(Square.__dict__)
pprint(Rectangle.__dict__)
