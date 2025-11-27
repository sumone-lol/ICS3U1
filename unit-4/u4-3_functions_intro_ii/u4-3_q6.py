'''
6. Write a function called angle(a,b,c) that will determine the measure of the
angle opposite side a in a triangle given side lengths a, b, and c as 
parameters and prints the result. Test your program with these values:
angle(3, 4, 5)
angle(4, 3, 5)
angle(5, 4, 3)
'''

import math

def angle(a, b, c): # using cosine law
    print("The angle opposite to side a (first number) is", \
        str(
            math.degrees(
                  math.acos((b**2 + c**2 - a**2) / (2 * b * c))
            )
        ) + chr(176))

angle(3, 4, 5)
angle(4, 3, 5)
angle(5, 4, 3)