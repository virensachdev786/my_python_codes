import copy
def main():
    a = [[1,2,3],[4,5,6],[7,8,9]]
    #copy.copy = shallow.copy(when copied it will not copy the whole thing)
    #deep.copy = will create a new membory space and copy the the whole thing
    b = copy.deepcopy(a)
    print("printing the value of a : {0}".format(a))
    print("printing the value of b : {0}".format(b))

    #appending list a
    a.append([10,11,12])
    print("printing the value of a after appending: {0}".format(a))
    print("printing the value of b: {0}".format(b))

    #changing the value of list a in first position
    a[1][0] = 10

    print("printing the value of a after editing : {0}".format(a))
    print("printing the value of b : {0}".format(b))

if __name__=="__main__":
    main()