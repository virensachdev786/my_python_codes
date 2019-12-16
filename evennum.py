def main():
    a = [1, 2, 3, 4, 5, 6, 7]
    b = list()

    for i in a:
        if(i % 2 == 0):
            b.append(i)

    print(b)

if __name__ == "__main__":
    main()