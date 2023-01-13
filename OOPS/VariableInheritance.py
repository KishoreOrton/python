class A:
    i, j = 10, 20


class B(A):  # Inheritance by using B(A)
    a, b = 5, 15

    def m1(self):
        print(self.a + self.b)  # accessing child class variable
        print(self.i + self.j)  # accessing parent class variable


OvrB = B()
OvrB.m1()  # Latest method will exe
