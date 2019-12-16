def main():
    #a and b arereference variables pointing to the same location
    a = [1,2,3,4]
    b = a
    print("initial value of a is :{0}".format(a))
    print("initial value of b is :{0}".format((b)))

    #appending a
    a.append(5)
    #printing a
    print("value of a after appending : {0}".format(a))
    #printing value of b
    print("value of b after appending a : {0}".format(b))

    #deleting the last element of the list in a
    a.pop()
    #printing value of a after appneding the last element of list
    print("value of a after deleting the last elemnt of list: {0}".format(a))
    #printing the value of b
    print("value of b after deleting the last element of b: {0}".format(b))

if __name__=="__main__":
    main()
