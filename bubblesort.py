def main():


    a = [1, 5, 6, 3, 2, 4]


    for i in range(len(a) - 1):

        for j in range(len(a) - i-1):#want j to dec by  every alteration
#logic for swapping numbers in list so that resolve comes out to be a acending  order
            if(a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j+1] = temp

    print(a)

if __name__=="__main__":
    main()

