def wrap2(func2):
    def wrapper2(a):
        print("i am in wrap 2")
        func2(a.upper())
        print("wrap 2 is execuited")
    return wrapper2

def wrap1(func):
    def wrapper(a):
        print("i am in wrap 1")
        func(a.split())
        print("wrap 1 is execuited")

    return wrapper

@wrap2
@wrap1
def gift(a):
    print("Printing the capital values : {0} ".format(a))

def main():
    gift("hello world")

if __name__=="__main__":
    main()