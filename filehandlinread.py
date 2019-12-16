def main():

    #storing the path and contents inside folder in f by writing the following statement and then printing it
    with open("/Users/virensachdev786/Desktop/Term/text.txt", "r") as f:
        print("\nReding the file.\n")

        # a = f.read()
        # print("Written lines is : \n{0}".format(a))
        #
        # b = a.split(" ")
        # print("The string as it is : {0}".format(b))

        c = f.readline()
        d = f.readline()
        e = f.readline()

        print(c.split(" "))
        print(d.split(" "))
        print(e.split(" "))



    #stoering the contents this time directly in file and printig it.
    # file = open("/Users/virensachdev786/Desktop/Term/text.txt", "r")
    # print(file.read())
    # file.close()




if __name__=="__main__":
    main()