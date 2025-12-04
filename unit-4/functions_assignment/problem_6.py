'''
Date: 2025-12-04

6. Write three functions called addNumbers, subtractNumbers, and calculate. 
The function addNumbers should take two numbers (x and y) as parameters and 
return the value of adding them together, while subtractNumbers should also 
take two numbers (x and y) and return the value of x minus y. Lastly, define a 
function called calculate that takes three numbers (a, b, and c) and uses 
addNumbers and subtractNumbers to add a and b and subtract c. The value should 
be returned. For example, calculate(2,3,4) should return 1.
'''

# Ask user for numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
num3 = int(input("Enter the third number: "))

# Arithmetic functions
def addNumbers(x, y):
    return x + y

def subtractNumbers(x, y):
    return x - y

def calculate(a, b, c):
    return subtractNumbers(addNumbers(a, b), c)

# Print result of (num1 + num2) - num3
# print(calculate(2, 3, 4))
print(f"The result of the calculation is {calculate(num1, num2, num3)}")