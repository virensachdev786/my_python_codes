def showMe(message):
    def inner():
        print(message)
    return inner

def main():
    c = showMe("Hello Wolrld")
    c()
    del showMe
    c()

if __name__=="__main__":
    main()