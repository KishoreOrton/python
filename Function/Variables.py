GlobalVar = "Global Variable"


def func():
    local_var = "Local Variable"  # Variable name should be in lower cases inside the funtion
    print(GlobalVar)
    print(local_var)


func()  # Calling the function

####################################################

# Global and local variable

xy = 100


def num():
    xy = 200  # This will print first because of local variable
    print(xy)


num()


# Change to Global variable
def gol():
    # Global xy = 300  # Invalid statement
    global xy
    xy = 300
    print(xy)


gol()

print("Access inside the function",xy)  # able to access xy inside the function because it is mentioned as global
