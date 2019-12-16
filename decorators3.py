def smartdiv(func):
    def wrapper(a,b):
        if b == 0:
            print("invalid input")
        else:
            print("Calculation being performed")
            func(a,b)
    return wrapper

@smartdiv
def divide(a,b):
    print(a/b)

def main():
    divide(10,5)

if __name__=="__main__":
    main()