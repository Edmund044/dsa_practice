from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,length,width):
        self.length = length
        self.width = width


    def get_area(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self,length):
        self.length = length


    def get_area(self):
        return self.length**2
    

shape1 = Rectangle(5,4)
print(shape1.get_area()) 
shape2 = Square(3)
print(shape2.get_area())
        
