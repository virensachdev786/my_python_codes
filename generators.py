def abc():
    n = 0
    print("printing first value of n")
    yield n

    n = n + 1
    print("printing second value of n")
    yield n

    n = n + 2
    print("printing thrd value of n")
    yield n


def main():
    a = abc()
    print(a.next())
    print(a.next())
    print(a.next())
    print(a.next())



if __name__=="__main__":
    main()