#importing module from other program
from venv.OOPS8myconfig import MyConfig

class BankAccount(object):

    #the init statement
    def __init__(self,name):
        self.balance = 0
        self.minbalance = 50
        self.name = name


    #defining deposite( logic: balance = balance + value entered for deposit )
    def deposit(self,d):
        self.balance = self.balance + d

    #defining withdraw( logic: temp is temp. variable where if less than 50 , bal. will not be withdrawn, else balance = balance - wntered withdrawn amount)
    def withdraw(self,w):
        temp = self.balance - w
        if(temp < self.minbalance):
            print("can not withdraw")
        else:
            self.balance = self.balance - w

    #defining balance(logic = jsut printing balance as it was automatically updated)
    def bal(self):
        print("remaining balance is {0} ".format(self.balance))

def main():

    #taking input
    print("Enter name: ")
    name = input()

    #conditions for entering the correct name
    if name in MyConfig.USERS.keys():
        if(name == 'Mukesh'):
            main_user_obj = BankAccount(name)
            print("welcome {0}".format(main_user_obj.name))

        elif(name == 'Manish'):
            main_user_obj = BankAccount(name)
            print("welcome {0}".format(main_user_obj.name))

        else:
            print("User doesnt match")
            exit()
    else:
        print("User does not exit!.")
        exit()

    #while loop for the options
    i = 0
    while(i == 0):

        print("Choices:            \
                \n 1.deposit       \
                \n 2.withdraw      \
                \n 3.showbalance   \
                \n 4.exit")

        print("enter your choice: ")
        option = int(input())


        if(option == 1):
            print("enter deposit amount: ")
            d = int(input())
            print("Amount depsoited {0} ".format(d))
            main_user_obj.deposit(d)

        if(option == 2):
            print("enter amount to be withdrawn: ")
            w = int(input())
            print("withdrawn amount is {0}".format(w))
            main_user_obj.withdraw(w)

        if(option == 3):
            main_user_obj.bal()

        if(option == 4):
            print("THANK FOR USING BANK : {0}".format(main_user_obj.name))
            break



if __name__=="__main__":
    main()