'''
2. a) Write a program that reads five marks and computes the average. Use the 
sample code from today's lesson on adding three numbers to help you get started
'''

marks = []

for i in range(5):
    marks.append(float(input("Enter a mark: ")))
average = sum(marks) / 5

print(f"The average of the 5 marks is {round(average)}%")