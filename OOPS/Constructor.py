class subject:
    def __init__(self):
        print("The First Constructor")

    def method_name(self):
        print("This is method")


Run = subject()  # constructor will invoke while creating object itself
Run.method_name()  # Calling the method

print("===========================")


# Multiple constructor
class Student:
    name = "Kishore Class"

    def __init__(self):
        print("The First Constructor")

    def __init__(self):
        print("The second contractor")

    def __init__(self, name):
        print("The second contractor", name)
        print(self.name)


st = Student("Kishore const")  # Passing parameter to the constructor


# unintended does not match any outer indentation level - Error means installment and blocks should check

print("===========================")

# Example of constructor

class emp:

    def __init__(self, eid, name, sal):  # for the parameter we need variable which should be inside the class
        self.eid = eid
        self.name = name
        self.sal = sal  # This will be a class variable if we use self,class_variable_name = variable
        print("Constructor", eid, name, sal)

    def display(self):
        print("Methods", self.eid, self.name, self.sal)


Emp = emp(101, "Kishore", 54.000)
Emp.display()

print("===========================")

# Example of constructor [Same as above adding one more constructor to print the data of strings]

class emp:

    def __init__(self, eid, name, sal):  # for the parameter we need variable which should be inside the class
        self.eid = eid
        self.name = name
        self.sal = sal  # This will be a class variable if we use self,class_variable_name = variable
        print("Constructor", eid, name, sal)

    def __str__(self):
        print(self.name)

    def display(self):
        print("Methods", self.eid, self.name, self.sal)


Emp = emp(101, "Kishore Kumar", 54.000)
Emp.display()

print(Emp)  # Just give print with the variable to invoke print
