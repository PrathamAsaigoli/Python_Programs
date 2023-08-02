import math
class shape:
    def __init__(self):
        self.area=0
        self.name=" "

    def showArea(self):
        print("The area of the shape ", self.name, "is", self.area, "units")

class Circle(shape):
    def __init__(self,radius):
        self.area=0
        self.name="Circle"
        self.radius=radius
    def calcArea(self):
        self.area= math.pi*self.radius*self.radius

class Rectangle(shape):
    def __init__(self,length,breadth):
        self.area=0
        self.name="Rectangle"
        self.length = length
        self.breadth = breadth
    def calcArea(self):
        self.area= self.length*self.breadth

class Triangle(shape):
    def __init__(self,base,height):
        self.area=0
        self.name="Triange"
        self.base=base
        self.height=height
    def calcArea(self):
        self.area=self.base*self.height/2

c1=Circle(2.5)
c1.calcArea()
c1.showArea()

r1=Rectangle(1.5,1.5)
r1.calcArea()
r1.showArea()

t1=Triangle(5.5,3.27)
t1.calcArea()
t1.showArea()