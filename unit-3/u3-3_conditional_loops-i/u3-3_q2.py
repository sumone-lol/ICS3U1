# 2. Write a program that multiplies a given integer by three until it exceeds 10000.

x = int(input("Enter an integer: "))

while x < 10000:
    x *= 3
    print(x)