#a = [ "hi" , "this" , "is" , "a" , "simple" , "string" , "we" , "have" , "on", "us" ]
#x = "hello"
#y = "wolrd"
# x + y

#filter = find only strings with length less than equl to (use len() func)
#map = add space in end of each string you get from filter
#reduce = concanate the result using '+' & print find statement`

def main():

    a = ["hi" , "this" , "is" , "a" , "simple" ,"string","we","have","on", "us"]
    #print("string entered is{0} ".format(a))

    #b = filter(lambda x : x if(len(x) <= 2) else None , a)
    #print("this is the filtered string:{0}".format(b))

    #c = map((lambda y : y+" ") , filter(lambda x : x if(len(x) <= 2) else None , a))
    #print(c)


    #we can use the filter fun with lambda function with just the comdition below and without if and else statemets.
    d = reduce(lambda p, m: p + m, map((lambda y : y+" ") , filter(lambda x : (len(x) <= 2), a)))
    print(d)

if __name__=="__main__":
    main()