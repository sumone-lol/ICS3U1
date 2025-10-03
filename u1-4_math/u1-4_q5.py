'''
5. Write a program that will ask the user for the length and width of a 
rectangle. The program will then calculate the perimeter and area and output 
the results clearly.
'''

length = float(input("What is the length of the rectangle?\n"))
width = float(input("What is the width of the rectangle?\n"))

area = round(length * width, 2)
perimeter = round(2 * (length + width), 2)

print("\nThe area of the rectangle is", str(area) + "^2")
print("The perimeter of the rectangle is", perimeter)