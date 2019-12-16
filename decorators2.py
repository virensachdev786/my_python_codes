def wrapitUp(func):
    def wrapper(x):
        print("from decorator : {0}".format(x))
        func(x)
    return wrapper

@wrapitUp
def gift(x):
    print("From gift")
    print(x)

def main():
    gift("Hello World")

if __name__=="__main__":
    main()