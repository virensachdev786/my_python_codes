def checknum(a):

    if(a % 2 == 0):
        return 0


def main():
    print("enter a number: ")
    num = int(input())
    a = num

    c = checknum(a)

    if(c == 0):
        print("number is even")
    else:
        print("number is odd")


if __name__=="__main__":
    main()