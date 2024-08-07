#Define a class named Shape and its subclass Square:

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    
    def area(self):
        return self.length * self.length

shape = Shape()
square = Square(4)

print(f"Area of shape: {shape.area()}")
print(f"Area of square: {square.area()}")
