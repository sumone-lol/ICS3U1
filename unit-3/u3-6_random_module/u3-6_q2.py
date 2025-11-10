'''
2. Write programs to accomplish each task.
a) Generate a random floating-point value f such that 5 ≤ f < 15.
b) Generate a random tax rate between 10 and 20%, then calculate the tax
on an item whose price is determined by the user.
c) Make two random selections from the letters in your name, then
check if they are the same.
d) Generate three random letters, and check if exactly two of them are
vowels.
'''

import random


f = random.randrange(5,15)

print(f"f = {f}")


print("\n----\n")
# -------------------------------------

price = round(float(input("Enter the cost of the item: $")),2)
tax = random.randrange(1.1,1.2)
total = price * tax

print(f"The total cost is {total}, calculated with a tax of {(tax - 1) * 10}%")


print("\n----\n")
# -------------------------------------

name = "your name"
letter1 = random.choice(name)
letter2 = random.choice(name)

print(f"Two letters same in {name}? {letter1 and letter2}")


print("\n----\n")
# -------------------------------------

letter_dict = "abcdefghijklmnopqrstuvwxyz"
vowels_dict = "aeiou"
letters = []
vowels_count = 0
for i in range(3):
    letters.append(random.choice(letter_dict))
for i in vowels_dict:
    vowels_count += letters.count(i)
if vowels_count == 2:
    print(f"There are exactly 2 vowels in {letters}.")
else:
    print(f"There are not exactly 2 vowels in {letters}.")
    