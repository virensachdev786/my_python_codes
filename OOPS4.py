class Employee(object):

    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    def display(self):
        print("employe name is :{0}".format(self.name))
        print("employee salary is :{0}".format(self.salary))


def main():
    myobj = []
    name = []
    salary = list()

    for i in range(2): #adding objects to the list
        print("Enter name of employee {0} : ".format(i+1))
        temp1 = input()
        name.append(temp1)
        print("Enter Salary of employee {0} : ".format(i+1))
        temp2 = int(input())
        salary.append(temp2)
    #myobj = list of objects
    for i in range(2):
        myobj.append(Employee(name[i],salary[i]))

    #accessing objects from the list
    for i in range(2):
        myobj[i].display()




if __name__=="__main__":
    main()