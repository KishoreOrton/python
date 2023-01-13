print("Example 1")


class Calculate:
    def add(self, a, b, c=0):
        if c > 0:
            print("a + b + c = ", a + b + c)
        else:
            print("a + b = {}".format(a + b))              # another method to use the variable


c1 = Calculate()
c1.add(10, 20, 30)
c1.add(10, 20)

print("Example 2")


class Employee:
    def Hello_Emp(self, e_name=None):
        if e_name is not None:
            print("Hello " + e_name)
        else:
            print("Hello ")


emp1 = Employee()
emp1.Hello_Emp()
emp1.Hello_Emp("Kishore Kumar")
