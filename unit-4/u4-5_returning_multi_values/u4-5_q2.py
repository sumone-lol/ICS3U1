'''
2. Write a function quot_rem(num1, num2) that takes two numbers as parameters
and returns the quotient and remainder when num1 is divided by num2. Test this
function in the main program with at least the following values:

num1    num2    Quotient and Remainder
7       2       3 and 1
18      5       3 and 3
72      12      6 and 0
0       12      0 and 0
3       8       0 and 3
3       0       error
'''

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

def quot_rem(num1, num2):
    try:
        return num1 // num2, num1 % num2
    except:
        return ArithmeticError

try:
    quot, rem = quot_rem(a, b)
    print(f"Quotient: {quot}\nRemainder: {rem}")
except:
    print("Error")