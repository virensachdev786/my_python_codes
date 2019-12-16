class ABC(object):

    #initialization
    def __init__(self, val):
        self.number = val

    #returing the object
    def __iter__(self):
        self.iter = [1, 2]
        return self

    #putting the logic
    def next(self):
        if (self.number == self.iter):
            raise StopIteration
        else:
            return self.iter * 3
            #return self.iter ** 2

def main():
    ABCobj = ABC(4)
    myiter = iter(ABCobj)
    print(myiter.next())
    print(myiter.next())
    print(myiter.next())
    print(myiter.next())
    #print(myiter.next())


if __name__=="__main__":
    main()