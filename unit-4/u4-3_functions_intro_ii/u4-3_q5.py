'''
5. Write a function called area(a, b, c) that will calculate the area of a 
triangle given the side lengths a, b, and c as parameters and prints the 
result. You need to do trigonometry to determine the height! Test your program 
with these values: area(3, 4, 5) – the area should be 6.
'''

import math

def area(a, b, c): # Heron's formula
    s = (a + b + c) / 2
    print(f"Area: {math.sqrt(s * (s - a) * (s - b) * (s - c))}")

area(3, 4, 5)