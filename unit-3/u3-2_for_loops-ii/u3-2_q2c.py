'''
2. c) Modify the program to check if the mark entered is between 0 and 100. If 
the mark is not between 0 and 100, print an error message that says “You 
entered a mark that is not between 0 and 100. The calculated average may not 
make sense.”
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