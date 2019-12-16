def main():
    a = [1 , 2 , 3 , 4 ,5]

    print("\n")

    #inside c we are writing map as argument and filter as iterable.
    c = list(map(lambda x : x ** 2 , filter(lambda x : x if(x >= 3) else None , a)))
    print("squares of numbers more than or equal to 3 are: {0}".format(c))

    print("\n")

    #for y < 10
    e = list(filter(lambda y : y if(y<10) else None, map((lambda y : y ** 2) ,a)))
    print("filtered squares are:{0}".format(e))

    print("\n")

    #for sum of numbers less than 10 in list a
    f = reduce(lambda v , m : v + m , filter(lambda y : y if(y<10) else None, map((lambda y : y ** 2) ,a)))
    print("sum of numbers of squares less than 10 is :[{0}]".format(f))


if __name__=="__main__":
    main()
