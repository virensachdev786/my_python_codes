# def revstr(str):
#
#     for i in range(len(str)-1,-1,-1):
#         yield (str[i])



def main():
    # c = revstr('hello')
    # for i in range(len('hello')):
    #     print(c.next())

    a = [1,2,3,4,5]
    b = sum(i ** 2 for i in a)

    print(b)
    # try:
    #     while(True):
    #
    #         print(b)
    # except StopIteration:
    #     print("Finished")




if __name__=="__main__":
    main()