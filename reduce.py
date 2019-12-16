from functools import reduce

def main():

    a = [1 , 2 , 3 , 4]
    b = reduce(lambda x,y : x+y , a)

    print(b)

if __name__=="__main__":
    main()