'''
1. Use the random module to simulate each scenario.
a) Simulate the sum of the rolls of two dice, by generating a random
number between 2 and 12.
b) Simulate the sum of the rolls of two dice, by generating two
random numbers between 1 and 6, then adding them.
c) Explain how the two scenarios above are different, even though they
result in the same values. Which one is correct?
'''

import random

one_die = random.randint(2,12)
two_die = random.randint(1,6) + random.randint(1,6)
print(one_die, two_die)

'''
The two scenarios both provide a somewhat random number between 2 and 12, but
they have slightly different distributions. The two dice roll with an average 
of 7 while the single D12 rolls a slightly skewed average of 6.5.
'''