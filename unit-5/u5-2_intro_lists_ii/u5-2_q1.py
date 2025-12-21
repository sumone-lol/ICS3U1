# 1. Write the following functions

'''
a) linear_list(n) - This function returns a list that contains the integers 1 
to n. For instance, calling linear_list(8) in the main program will return
[1, 2, 3, 4, 5, 6, 7, 8]
'''

def linear_list(n):
    list = []
    for i in range(n):
        list.append(i + 1)
    return list


'''
b) random_list(n, m, k) – This function returns a list of n random integers
between m and k. For instance, calling create_random(10, 3, 12) will
create a list of 10 randomly generated integers between 3 and 12
'''

import random

def random_list(n, m, k):
    list = []
    for i in range(n):
        list.append(random.randint(m, k))
    return list


'''
c) user_list(n) – This function returns a list of n values as read in from the
user.
'''

def user_list(n):
    list = []
    for i in range(n):
        list.append(input(""))
    return list

num = int(input("Enter the number of values to input: "))

print(user_list(num))