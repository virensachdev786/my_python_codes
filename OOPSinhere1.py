class Person(object):

    def __init__(self, name):
        self.name = name

    def display(self):
        print("Name is : {0}".format(self.name))

    def isEmployee(self):
        print("False (I am in parent class)")

#inhereing Person class
class Employee(Person):

    def __init__(self, name1):
        super(Employee, self).__init__(name1)
        self.name1 = name1

    def isEmployee(self):
        print("True (I am in child class)")

    #def display(self):
    #    print("Name of employee is: {0}".format(self.name1))

def main():
    emp = Employee("Manish")
    emp.display()
    emp.isEmployee()

    per = Person("Harish")
    per.display()
    per.isEmployee()

if __name__=="__main__":
    main()
