def even(x):
    if(x % 2 == 0):
        return x

def sqr(a):
    return a ** 2

def main():
    a = [1,2,3,4,5]
    b = list(filter(even,a))
    print(b)

    c = list(map(even,a))
    print(c)

    d = list(filter(sqr,a))
    print("d={0}".format(d))

if __name__=="__main__":
    main()