def main():

    a = [1,2,3,4,5,6]
    b = [ x + 5 if x % 2 == 0 else x for x in a]#list compheration
    c = [ x ** 2 for x in a]

    print(b)
    print(c)

    name = "viren"
    # d = [ x for x in name if x !='r' ]
    # print(d)

    for i in name:
        if(i == 'e'):
            break
        print(i)


if __name__=="__main__":
    main()