class Point():
    def __init__(self,x) -> None:
        self.x = x    

    def __add__(self,other):
     return self.x + other.x   

p1 = Point(1)
p2 = Point(2)

print(p1 + p2)

        
            