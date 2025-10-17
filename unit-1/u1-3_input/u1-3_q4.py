'''
4. Write a program that prompts the user for 4 course marks. Each mark should 
be saved in a properly named variable such as mark1, mark2, mark3, mark4. Once 
the user has entered the last mark, output a summary of the marks.
'''
import statistics

mark = []

while True:
    buffer = input(
        "Enter a course mark to the nearest whole number. Enter 'e' once all "
        "marks are entered.\n"
    )
    if buffer == "e":
        break
    else:
        mark.append(int(buffer))

print("\nSummary of marks:", mark)
print("Average:", round(statistics.mean(mark), 2))