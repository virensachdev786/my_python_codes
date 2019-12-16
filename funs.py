

def sub(a,b):
    c = b - a
    return c

def mul(a,b):
    c = a * b
    return c

def div(a,b):
    c = a / b
    return c




def main():
    a = 10
    b = 13
    c = 10
    d = 5

    x = lambda a, b, c, d : a + b + c + d
    y = sub(a,b)
    z = mul(a,b)
    v = div(a,b)

    #print("sum :{0}".format(x))
    print("sum is: {0}".format(x(a,b,c,d)))
    print("subtracted :{0}".format(y))
    print("product :{0}".format(z))
    print("divided :{0}".format(v))

if __name__=="__main__":
    main()