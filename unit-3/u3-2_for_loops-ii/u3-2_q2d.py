'''
2. d) Modify the program to also output the lowest and highest mark
'''

marks_quantity = int(input("Enter the number of marks: "))
marks = []

for i in range(marks_quantity):
    marks.append(float(input("Enter a mark: ")))
    if marks[-1] < 0 or marks[-1] > 100:
        print("You entered an invalid mark (i.e. < 0 or > 100), " \
              "the calculated average may not make sense.")
average = sum(marks) / marks_quantity

print(f"The average of the {marks_quantity} marks is {round(average)}%")
print(f"The highest mark is {max(marks)}% and the lowest mark is {min(marks)}%")