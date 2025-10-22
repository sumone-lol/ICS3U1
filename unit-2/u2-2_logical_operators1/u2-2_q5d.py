# Write programs to accomplish each task.
# Determine if a given integer is not a multiple of 4 or 7.

num = int(input("Enter an integer\n"))

if not ((num % 4 == 0) or (num % 7 == 0)):
    print("This integer is not a multiple of 4 or 7")