print("Start Program")
try:
    print(x)  # Invalid statement due to try and except program is not terminated
except:
    print("Error occurred")

print("End of the Program")

# Example 10/0 this will give zero decision exception

print("Starts program")
x = input("Enter the number to divide by 10 : ")
try:
    print(10 / int(x))  # if we give input 0 then it shows ZeroDivisionError
except ZeroDivisionError:  # We can specify the name of the exception
    print("Exception Occurred -- Handled ")  # Except block will execute only if we have exception [In this example when
    # user input is O]
    print("End program")
