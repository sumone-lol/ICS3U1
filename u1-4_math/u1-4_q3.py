'''
3. Ask the user their name, age, and the current year. Greet the user and tell 
them the year they will be 25, 50, and 75.
'''
import time

current_year = time.localtime().tm_year
name = input("What is your name?\n")
age = int(input("How old are you?\n"))
birth_year = current_year - age

print("You will be age 25 in the year", str(birth_year + 25) + ", age 50 in the year",
      str(birth_year + 50) + ", and age 75 in the year", str(birth_year + 50) + "."
)
