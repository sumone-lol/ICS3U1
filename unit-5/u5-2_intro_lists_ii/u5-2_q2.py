import random

def linear_list(n):
    list = []
    for i in range(n):
        list.append(i + 1)
    return list

def random_list(n, m, k):
    list = []
    for i in range(n):
        list.append(random.randint(m, k))
    return list

def user_list(n):
    list = []
    for i in range(n):
        list.append(int(input("")))
    return list


# 2. Using the above functions, write the following programs.

'''
a) Read 10 integers from the user and store them in a 10-element list. 
Determine the following:
- the sum of the values
- the average of the values
- the highest and lowest values
- the number of odd and even values
'''

a = user_list(10)

sum = sum(a)
avg = sum / len(a)
highest = max(a)
lowest = min(a)
even = 0
odd = 0
for i in a:
    if i % 2 == 0:
        even += 1
    else:
        odd += 1

print(sum)
print(avg)
print(highest)
print(lowest)
print(even)
print(odd)


print("\n--------------------\n")
'''
b) Create a 5-element list containing 5 random integers between 1 and 5.
Determine if the elements are in descending order
'''

b = random_list(5, 1, 5)

# lol gonna study for a functions test idc