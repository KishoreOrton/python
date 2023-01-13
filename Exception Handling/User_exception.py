x = input("Number : ")

if int(x) < 0:
    raise Exception("Sorry, no numbers below zero")
else:
    print("Given number", x, "is greater / Equal to Zero")
