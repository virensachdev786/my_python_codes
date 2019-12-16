class Rectangle(object):

    def __init__(self,length,width):
        self.length = length
        self.width = width

    def calculate(self):

        self.area = self.length * self.width
        print("calculated area is: {0} ".format(self.area))

def main():


    print("enter the length: ")
    length = int(input())
    print("enter the width: ")
    width = int(input())
    obj = Rectangle(length,width)


    obj.calculate()



if __name__=="__main__":
    main()