class Functions(object):



    def __init__(self):
        a = [1,2,3,4,5,6]
        print("construct statement written")

    def filter(self):
        b = list(filter(lambda y: y if (y % 2 ==0) else None , Functions.a))
        print(b)

    def map(self):
        c = list(map(lambda v : v ** 2 , Functions.a))
        print(c)

    def reduce(self):
        d = reduce(lambda g,o : g+o , Functions.a)
        print(d)

def main():
    obj = Functions()
    obj.filter()
    obj.map()
    obj.reduce()

if __name__=="__main__":
    main()