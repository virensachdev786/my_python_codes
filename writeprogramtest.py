def main():

    with open("/Users/virensachdev786/Desktop/Term/testfilehowareyou.txt", "w")as f:
        a = "Hello how are you   i am viren"
        f.write(a.rstrip())

if __name__=="__main__":
    main()