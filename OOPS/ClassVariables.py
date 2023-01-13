class maths:
    a, b = 10, 20

    def add(self):
        print(self.a + self.b)

    def Mul(self):
        print(self.a * self.b)


M1 = maths()
M1.add()
M1.Mul()

# Global , Local and Class Variables

a, b = 10, 20


class allvar:
    i, j = 10, 5

    def method(self, x, y):
        print("Global variable", a + b)
        print("Class Variable", self.i + self.j)
        print(x + y)


Call = allvar()  # Call the method
Call.method(10, 20)

# same variable name

a, b = 10, 20


class allvar1:
    a, b = 10, 5

    def method(self, a, b):
        print("Global variable", a + b)
        print("Class Variable", self.a + self.b)
        print(a + b)


Run = allvar1()  # Call the method using variable name
Run.method(5, 10)
