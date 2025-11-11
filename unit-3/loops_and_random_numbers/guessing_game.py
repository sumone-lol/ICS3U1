'''
To create a number guessing game in Python, the random module is used to 
generate a random integer between 1-100. Store this number in a variable. Ask 
the user to guess the number between 1-100. Indicate if the guessed number is 
higher or lower than the generated random number. Give 5 attempts to guess  
the number. After that, display the correct number. If the user guessed it 
correctly in less than 5  of attempts, then congratulate him/her for guessing 
the number correctly..
'''

import random

# Initialize variables
answer = random.randint(1,100)
guess = 0
attempts = 0

# Ask user for guess within 5 attempts
while attempts < 5:
    guess = int(input("Guess the number (1-100): "))
    if guess > answer:
        print("Lower")
    elif guess < answer:
        print("Higher")
    else:
        print("Correct, congratulations!")
        attempts += 1
        break
    attempts += 1
    print(f"Attempts: {attempts}/5\n")

# Indicate results
if guess == answer:
    print(f"Attempts: {attempts}/5")
else:
    print(f"You ran out of your 5 attempts! The answer was {answer}")