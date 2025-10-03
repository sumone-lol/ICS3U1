'''
4. Write a program that will ask the user for the radius of a circle. The 
program will then calculate the circumference and area of the circle and 
output the results clearly.
'''

PI = 3.141592
radius = float(input("What is the radius of the circle?\n"))
circumference = 2 * PI * radius
area = PI * radius ** 2

print("\nThe circumference of the circle is", circumference)
print("The area of the circle is", area)