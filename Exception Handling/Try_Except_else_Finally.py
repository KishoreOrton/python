y = input("Enter the number to divide 10 : ")

try:
    result = 10 / int(y)        # Floor Division : Gives only Fractional
except ZeroDivisionError:
    print("Sorry ! You are dividing by zero ")
else:
    print("Yeah ! Your answer is :", result)
finally:
    # this block is always executed
    # regardless of exception generation.
    print('This is always executed')
