UserName = input("Enter the UserName ")
PhoneNumber = input("Enter the PhoneNumber ")
Email = input("Enter the Email ")

# The data type will consider as string for user input even the user enters number also
print(type(PhoneNumber))

print("Name of the user is {} , Mobile number : +91{} and Email ID - {}".format(UserName, PhoneNumber, Email))

# Other methods
print(str(UserName))
print(int(PhoneNumber))