from math import pi

class Circle(object):

    def __init__(self,radius):
        self.radius = radius


    def display(self):
       self.area = pi * self.radius ** 2
       print("area of circle is : {0}".format(self.area))

def main():


    print("enter the radius of circle: ")
    radius = int(input())
    obj = Circle(radius)

    obj.display()

if __name__=="__main__":
    main()

