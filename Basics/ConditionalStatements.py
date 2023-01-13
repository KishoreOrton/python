age = input("Enter the age : ")
num = input("Enter the num : ")

# and - Both condition is TRUE
# OR - Any one condition is TRUE


if int(age) >= 18 and int(age) <= 105:
    print("Right to vote")
elif int(age) <= 0 or int(age) > 105:
    print("Invalid age")
else:
    print("Not the age to vote")

if int(num) % 2 == 0:
    print("Even")
else:
    print("Not Even")

# ternary Operator
print("Even") if int(num) % 2 == 0 else print("ODD")

var = {print("EVEN"), print("EVEN Number")} if int(num) % 2 == 0 else {print("ODD"), print("ODD Number")}
