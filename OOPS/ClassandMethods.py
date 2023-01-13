class Animals:
    def lion(self):  # default keyword self
        print("Am lion")
        pass  # Pass means null

    def Tiger(self, Type):  # With arguments
        print("Am", Type, "Tiger")


Ani = Animals()  # Keep the object in the variable
Ani.lion()  # Calling the method
Ani.Tiger("White")


# Instance method and static method


# Instance - we can call only through method     - using method
# Static - Directly call using class   [Annotation @staticmethod]   - using class

class LocalAnimals:
    def Deer(self):  # default keyword self
        print("Am Deer")
        pass  # Pass means null

    @staticmethod
    def Bear(self, Type):  # With arguments
        print("Am", Type, "Bear", "Total of ", self)


LA = LocalAnimals()
LA.Deer()
LocalAnimals.Bear(10, "Black")  # using the class name we are invoking due to static

