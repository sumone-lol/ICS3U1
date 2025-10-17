'''
1. Use if statements in programs to accomplish each task.
a. Output "GREATER" if a given integer is greater than 50.
b. Output "OTHER" if a given integer has any value other than 12.
c. Output "HIGHER" if a given integer is higher than 10, "LOWER" if it is
lower than 10, or "EQUAL" if equal to 10
'''

number = int(input("Enter an integer\n"))

if number > 50:
    print("GREATER")
if number != 12:
    print("OTHER")
if number > 10:
    print("HIGHER")
elif number < 10:
    print("LOWER")
else:
    print("EQUAL")