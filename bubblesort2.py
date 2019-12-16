def bubblesort(a):
    for i in range(len(a) - 1):

        for j in range(len(a) - i - 1):
            if (a[j] > a[j + 1]):
                temp = a[j]
                a[j] = a[j + 1]
                a[j + 1] = temp


def main():
    a = [6, 4, 3 ,1, 2, 5]
    bubblesort(a)
    print("Sorted list is {0}".format(a))

if __name__ == "__main__":
    main()
