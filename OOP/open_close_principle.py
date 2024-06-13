from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self,shape_type) -> None:
        self.shape_type = shape_type

    @abstractmethod
    def calculate_area(self):
        pass

class Rectangle(Shape):
    def __init__(self,width,length) -> None:
        super().__init__("Rectangle") 
        self.width = width
        self.length= length

    def calculate_area(self):
        return self.width * self.length


class Square(Shape):
    def __init__(self, side) -> None:
        super().__init__("Square")
        self.side = side

    def calculate_area(self):
        return self.side **2


shape1 = Rectangle(5,4)
print(shape1.calculate_area())      
shape2 = Square(3)
print(shape2.calculate_area())     


    