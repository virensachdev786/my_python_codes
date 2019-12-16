class ABC(object):
    def __init__(self):
        pass


    #class method has 2 types i.e static method and class method
    @staticmethod
    def hello():
        print("hello i am inside hello !")

    @classmethod
    def hello2(cls):
        print("hello i am inside hello2 !")
        print(cls)


def main():
    obj1 = ABC()

    #through the class name we can also call the class method
    ABC.hello2()

    #through the class name we can call the static method
    ABC.hello()

if __name__=="__main__":
    main()
