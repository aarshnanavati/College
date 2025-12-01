#  Create a class paper with width and height as data Member. Create function outside a class that
# find out area and perimeter of that paper Pass object as argument.
# area=weight*height, perimeter=2+width+height

class Paper:
    def __init__(self,width,height):
        self.width = width
        self.height = height

def findArea(p):
    area = p.width * p.height
    return area

def findPerimeter(p):
    perimeter = 2 * (p.width + p.height)
    return perimeter

n1 = int(input("Enter number 1: "))
n2 = int(input("Enter number 2: "))

p1 = Paper(n1,n2)
print("Width : ",p1.width)
print("Height: ",p1.height)
print("Area : ",findArea(p1))
print("Perimeter: ",findPerimeter(p1))