'''
4. Determine the time for an object, thrown with velocity v from an initial 
height h, to hit the ground using the formula: −4.9𝑡^2 + 𝑣𝑡 + ℎ = 0. Hint: Use 
quadratic formula. Name the function find_time(v, h) and return time. In the 
main program, test your function with these values: v=10, h=1. The answer 
should be 2.14.
'''
# SPH3U flashbacks
# [-b +- sqrt(b^2 - 4ac)] / 2a

import math

def find_time(v, h):
    time1 = (-v + math.sqrt(v ** 2 - 4 * -4.9 * h)) / (2 * -4.9)
    time2 = (-v - math.sqrt(v ** 2 - 4 * -4.9 * h)) / (2 * -4.9)

    return max(time1, time2)

print(find_time(10, 1))