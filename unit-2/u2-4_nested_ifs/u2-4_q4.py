# 4. What does this code do? Rewrite the code using the logical operator OR.
'''
letter = input("Please enter an uppercase letter: ")
if (letter != "A"):
    if (letter != "E"):
        if (letter != "I"):
            if (letter != "O"):
                if (letter != "U"):
                print(letter, "is a consonant.")
'''
# This code asks the user for an uppercase letter. If that letter is not A, 
# not E, not I, not O, and not U, it tells the user that the  is 
# a consonant.

letter = input("Please ente r an uppercase letter: ")

if letter != "A" or \
    letter != "E" or \
    letter != "I" or \
    letter != "O" or \
    letter != "U":
        print(letter, "is a consonant.")