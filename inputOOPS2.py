
class Userinput():

    def __init__(self):
        print("enter a number: ")
        self.a = int(input())


    def input(self):
        variable = self.a
        print("entered number is : {0}".format(self.a))

def main():
    obj = Userinput()
    obj.input()

if __name__=="__main__":
    main()