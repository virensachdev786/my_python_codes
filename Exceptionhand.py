def main():
    try:


        a = (1,2,3,4,5)
        b = a.append(6)
        print(a)

    except Exception as e:
        print("you can't add elements in a tuple")
        print("exception is {0}".format(e))

    # else:
    #     print("Running program")

    print("Program is continueing ")

if __name__=="__main__":
    main()