class Point(object):

    def __init__(self,x,y):
        self.x = x
        self.y = y

    #def __str__(self):
        #print("{0},{1}".format(self.x,self.y))

    # def __add__(self,secondobj):
    #     a = self.x + secondobj.x
    #     b = self.y + secondobj.y
    #     return (a,b)
    #
    def __sub__(self, secondobj):
        a = self.x - secondobj.x
        b = self.y - secondobj.y
        return (a,b)

    # def __mul__(self, secondobj):
    #     a = self.x * secondobj.x
    #     b = self.y * secondobj.y
    #     return (a,b)
    #
    # def __divmod__(self, secondobj):
    #     a = self.x % secondobj.x
    #     b = self.y % secondobj.y
    #     return (a,b)
    #
    # def __pow__(self, secondobj):
    #     a = self.x ** secondobj.x
    #     b = self.x ** secondobj.y
    #     return (a,b)

def main():
    obj1 = Point(1,2)
    obj2 = Point(3,4)

    # a = obj1.x + obj2.x
    # b = obj1.y + obj2.y
    # print(a,b)
    #obj.display()

    # print(obj1 + obj2)
    # print(obj1 - obj2)
    # print(obj1 * obj2)
    # print(obj1 % obj2)
    #print(obj1 ** obj2)

if __name__=="__main__":
    main()