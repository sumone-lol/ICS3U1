'''
3. a) Write a program that keeps asking the user for their name until they enter "Tim".
Otherwise, keep saying "You are not Tim!" and ask for their name.
b) Allow your name as a valid input as well.
c) Keep track of how many times the user fails to enter the correct name, and report it when they
finally get it right.
'''

name = input("Enter your name").lower()
attempts = 1

while name != "tim" or name != "your name":
    print("You are not Tim!")
    name = input("Enter your name").lower()
    attempts += 1
print(f"Attempts: {attempts}")