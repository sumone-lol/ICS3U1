'''
1. Have the user enter two integers between 1 and 9. Do the basic math 
operations using these numbers and display the answer (add, subtract, 
multiply, divide, exponent). For example, if the user entered the numbers 2 
and 3, you would output the results of 2+3, 2-3, 2*3, 2/3 and 2^3 (2 to the
exponent 3).
'''

int1 = int(input("Enter an integer\n"))
int2 = int(input("Enter another integer\n"))
print(int1, "+", int2, "=", int1 + int2)
print(int1, "-", int2, "=", int1 - int2)
print(int1, "*", int2, "=", int1 * int2)
print(int1, "/", int2, "=", int1 / int2)
print(int1, "^", int2, "=", int1 ** int2)