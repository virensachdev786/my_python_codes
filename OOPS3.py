class Employee(object):

    def __init__(self,n,s):
        self.name = n
        self.salary = s



    def display(self):
        print("name of Employee: {0} ".format(self.name))
        print("salary of employe: {0} ".format(self.salary))


def main():
    empobj = Employee("mainsh",1000000)
    empobj2 = Employee("viren",1000000)
    name = raw_input("enter name of Employee")
    salary = raw_input("enter salary of employee")

    empobj.display()
    empobj2.display()



if __name__=="__main__":
    main()
