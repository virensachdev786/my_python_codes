def sqr(a):
    return a ** 2

def even(a):
    if(a % 2 == 0):
        return a


def main():
    a = [1,2,3]
    b = (map(sqr, a))#map works in funs and iterables , iterables are passed to functions one by one and we get the result
    print(b)

    c = list(filter(even,a))
    print(c)

if __name__=="__main__":
    main()




