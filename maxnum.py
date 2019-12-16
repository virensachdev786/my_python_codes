#max is empty list, inside loop max goes to i, and print max
def main():
    a = [1, 2, 3, 4, 5, 6, 1, 8, 7]
    max = a[0]
    for i in a :
        if(i > max):
            max = i

    print(max)

if __name__=="__main__":
    main()