def main():
    a = [1 , 2 , 3 , 4]

    b = list(filter(lambda x : x if(x % 2 == 0) else None , a))
    print("filter is{0}".format(b))

    reduce

if __name__=="__main__":
    main()