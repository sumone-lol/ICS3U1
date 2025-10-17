'''
4. Ask the user to enter two different numbers, and have your program tell them
which number is the smaller of the two.
'''

num1 = float(input("Enter a number\n"))
num2 = float(input("Enter another number\n"))

if num1 < num2:
    print(f"{num1} is less than {num2}")
elif num1 > num2:
    print(f"{num2} is less than {num1}")
else:
    print("idk")