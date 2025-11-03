'''
2. b) Modify the program to ask the user how many marks there are.
'''

marks_quantity = int(input("Enter the number of marks: "))
marks = []

for i in range(marks_quantity):
    marks.append(float(input("Enter a mark: ")))
average = sum(marks) / marks_quantity

print(f"The average of the {marks_quantity} marks is {round(average)}%")