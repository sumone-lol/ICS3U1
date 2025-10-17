'''
6. A user inputs his age and if the user is under 16, display the message "You're
too young to drive." If the user is 16 or older then display an appropriate
statement.
'''

age = int(input("Enter your age\n"))

if age < 16:
    print("You're too young to drive")
else:
    print("an appropriate statement")