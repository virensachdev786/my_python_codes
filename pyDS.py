def main():

    #LIST
    # print("Enter the size of list")
    # n = int(input())
    # a = list()
    #
    # for i in range(n):
    #     print("enter elements of list: ")
    #     c = int(input())
    #     a.append(c)
    #
    # print("the entered list is: {0} ".format(a))

    #Tuple
    # print("Enter size of tuple: ")
    # t = int(input())
    # v = tuple()
    #
    # for i in range(t):
    #     print("Enter elements of tuple: ")
    #     v = list(v)
    #     m = int(input())
    #     v.append(m)
    #
    # v = tuple(v)
    #
    # print("the entered tuple is: {0}".format(v))

    #Dictionary
    mydict = dict()
    for i in range(2):
        print("Enter first name : ")
        firstname = input()

        print("Enter Last name : ")
        lastname = input()

        mydict[firstname] = lastname

    print("my dict is {0}".format(mydict))

    for key,value in mydict.items():
        print("{0} {1}".format(key,value))



if __name__=="__main__":
    main()
