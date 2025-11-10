'''
3. Use the random module to simulate flipping a coin 20 times. Print the
sequence of tosses, and calculate the following – hint – use a FOR
LOOP
a) the number of heads flipped
b) the number of tails flipped
'''

import random

heads = 0
tails = 0

for i in range(20):
    coin = random.choice([True,False])
    if coin:
        print("Heads")
        heads += 1
    else:
        print("Tails")
        tails += 1
print(f"\nTotal heads: {heads}\nTotal tails: {tails}")
