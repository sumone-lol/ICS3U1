'''
3. Write a function roots(a, b, c) that takes the coefficients of a quadratic 
equation in standard form as parameters and returns the real roots of the 
quadratic equation. Test this function in the main program with the following 
values:

a       b       c       Roots
1       -4      4       2 and 2
1       3       -5      1.19 and -4.19
1       1       1       error
'''

import math

quad_a = float(input("Enter a: "))
quad_b = float(input("Enter b: "))
quad_c = float(input("Enter c: "))

def roots(a, b, c):
    try:
        return \
            (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a), \
            (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
    except:
        return ArithmeticError

try:
    root1, root2 = roots(quad_a, quad_b, quad_c)
    print(f"{round(root1, 3)}\n{round(root2, 3)}")
except:
    print("Error")