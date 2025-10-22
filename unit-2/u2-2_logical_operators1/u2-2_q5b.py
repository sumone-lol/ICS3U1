# Write programs to accomplish each task
# Determine if a given integer is divisible by either 3 or 5.

num = int(input("Enter an integer\n"))

if (num % 3 == 0) or (num % 5 == 0):
    print("This integer is divisible by 3 and/or 5")