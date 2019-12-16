def main():
    a = []
    for i in range(5):
        c = int(input())
        a.append(c)

    print("my list is:{0}".format(a))
    min = a[0]
    for i in a:
        if(i < min):
            min = i

    print(min)

if __name__ =="__main__":
    main()