class BankAccount(object):

    def __init__(self):
        print("              WELCOME TO BANK             ")



    def deposit(self, dep):
        self.deposit = dep
        print("BALANCE IS : {0}".format(self.deposit))


    def withdra(self, w):
         print("{0} IS WITHDRAWN".format(self.w))



    def balanc(self, bal):
        self.balance = self.withdraw
        print("BALANCELEFT IS : {0}".format(self.balance))


def main():
    print("Enter amount for deposite: ")
    dep = int(input())
    obj = BankAccount()
    obj.deposit(dep)


    print("Enter amount for withdraw: ")
    w = int(input())
    obj = BankAccount()
    obj.withdra(w)


    print("Final balance is: ")
    bal = w
    obj = BankAccount()
    obj.balanc(bal)



if __name__=="__main__":
    main()

