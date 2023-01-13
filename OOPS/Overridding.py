class A:
    def m1(self):
        print("Method 1 ")


class B(A):  # Inheritance by using B(A)
    def m1(self):
        print("Overriding Method 1")


OvrB = B()
OvrB.m1()  # Latest method will exe

# If we want to invoke the parent method only [Use super()]
print("-----")


class C(A):  # Inheritance by using B(A)
    def m1(self):
        print("Overriding Method 1")
        super().m1()  # This will call the parent method


OvrC = C()
OvrC.m1()  # This will call the parent method

print("---# Overriding the variable name---")


class X:
    name = "Kishore"


class Y(X):
    name = "Kishore Kumar"

    def test(self):
        print(super().name)


name = Y()
print(name.name)

name.test()  # Access the parent class variable is not possible
# To access the parent we need one method it is indirect steps
