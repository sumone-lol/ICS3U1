# 4. Write a program that asks the user the same single, simple, math problem 
# until they get it right.

x = float(input("List the first 67 digits of pi? (65 decimal places)\n"))

while x != 3.14159265358979323846264338327950288419716939937510582097494459230:
    print("Incorrect, try again.")
    x = float(input("List the first 67 digits of pi? (65 decimal places)\n"))
print("congrats")
print("no, the 67 was not intentional, it's just the 80 cols max convention")