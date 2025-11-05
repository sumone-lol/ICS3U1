'''
2. Read n integers from the user and then sum the squares of all integers. If 
the user enters a negative integer, calculate the sum of the squares up until 
that point and end then end the program.
'''

integers = [0]

while integers[-1] >= 0:
    integers.append(int(input("Enter a positive integer, or "
                              "enter a negative integer to end the program: ")))
integers.pop()
for i in range(len(integers)):
    integers[i] **= 2
calculation = sum(integers)

print(f"The sum of the squares of all the integers is {calculation}.")