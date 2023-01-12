class Rectangle:
    pass


class Square(Rectangle):
    pass


print(issubclass(Rectangle, object))
print(issubclass(Square, object))
print(issubclass(Square, Rectangle))
print(issubclass(Rectangle, Square))
