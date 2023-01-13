# This will break the statement

for i in range(10):
    if i == 5:
        break
    print(i)
print("Completed")

# This will cont the statement and the i = = 5 is skipped

for i in range(10):
    if i == 5 or i == 4:
        continue
    print(i)
print("Completed")
