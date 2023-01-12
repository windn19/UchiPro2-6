class Rectangle:
    pass


class Square(Rectangle):
    pass


square = Square()
rectangle = Rectangle()

print(isinstance(rectangle, object))
print(isinstance(square, object))
print(isinstance(square, Rectangle))
print(isinstance(rectangle, Square))
