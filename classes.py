class hello(object):
    a = 5


    def __init__(self):
        self.b = 6
        print("i am in constroctor")

    def display(self):
        self.c = self.b + 1
        print("printing the value of c: {0}".format(self.c))
        print("type of variable entered: {0}:".format(type(self.c)))

    def viren(self):
        self.v1 = "viren"
        self.v = 1234
        print("printing the value of self.v: {0}".format(self.v))
        print(id(self.v))
        print("printing the address of self.v: {0}".format(id(self.v1)))

def main():
    obj = hello()

    obj.b = 90

    hello.a = 80

    obj.display()
    obj.viren()

    print(hello.a)

if __name__=="__main__":
    main()