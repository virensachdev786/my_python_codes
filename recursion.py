def fact(x):
    if(x == 1):
       return x
    else:
        return x * fact(x - 1)



def main():
    num = 5
    c = fact(num)
    print(c)

if __name__=="__main__":
    main()