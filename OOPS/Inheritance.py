print("-------------# Single inheritance---------------------")


# Single Inheritance

class A:
    def m1(self):
        print("Method 1 on class A [Parent class]")


class B(A):  # Inheritance by using B(A)
    def m2(self):
        print("Method 2 on class B [Child class]")


child_class_obj = B()  # Creating a obj using child class to access child and parent
child_class_obj.m1()  # Access all the methods from parents
child_class_obj.m2()

print("-------------# Multi level inheritance---------------------")


# Multi level inheritance
class addition:
    x, y = 10, 20

    def add(self):
        print(self.x + self.y)


class multiplication(addition):
    a, b = 5, 5

    def mul(self):
        print(self.a * self.b)


class Subraction(multiplication):
    s, d = 5, 10

    def sub(self):
        print(self.s - self.d)


Access = Subraction()
Access.add()
Access.mul()
Access.sub()

print("-------------Hierarchy Inheritance-------------------")

# Hierarchy Inheritance

class X:
    def mx1(self):
        print("Method 1 on class X [Parent class]")


class Y(X):
    def mx2(self):
        print("Method 2 on class X [Child class]")


class Z(X):
    def mx3(self):
        print("Method 2 on class X [Child class]")


child_Y =Y()  # Creating a obj using class Y
child_Z =Z()  # Creating a obj using class Z because it is inherited to X and Not to Y so u can't access Y
child_Z.mx1()
child_Z.mx3()
child_Y.mx1()
child_Y.mx2()

print("--------------Multiple Inheritance--------------------")

# Multiple Inheritance

class XX:
    def xxmethod(self):
        print("Parent class 1")


class YY:
    def yymethod(self):
        print("Parent class 2")


class ZZ(XX,YY):
    def zzmethod(self):
        print("Child for above 2 parents")


XXX = ZZ()
XXX.xxmethod()
XXX.zzmethod()
XXX.zzmethod()

