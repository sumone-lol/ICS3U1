# 1. Write programs to solve each task.

'''
a) Create a 5-element list, initialized with asterisks and then do the 
following:
- print the length of the list
- change the third element to #
- print the third element in the list
- print the last element in the list
'''

a = ["*","*","*","*","*"]
a[2] = "#"
print(a[2])
print(a[-1])


'''
b) Create a 5-element list, initialized with zeroes and then do the following
- change the first element to 7
- change the fourth element to “dog”
- use a for loop and print the list
'''

b = [0,0,0,0,0]
b[0] = 7
for i in b:
    print(i, end=" ")
print()


'''
c) Create a list that contains the letters in the word “Minecraft”. Then use 
slicing to print out the word “Mine” and the word “Craft
'''

c = []
for i in "Minecraft":
    c.append(i)

for i in c[0:4]:
    print(i, end="")
print()
for i in c[4:]:
    print(i, end="")
print()


'''
d) Create two lists … one initialized with 0’s and the other initialized with 
1’s. The zero_list should have 7 elements and the one_list should have 6
elements. What would be the output of the following commands?
- print(zero_list + one_list)
- print(zero_list*3)
- print(one_list + zero_list)
- print(zero_list + [2, 2, 2])
'''

d0 = [0, 0, 0, 0, 0, 0, 0]
d1 = [1, 1, 1, 1, 1, 1]

print(d0 + d1)
print(d1 * 3)
print(d1 + d0)
print(d0 + [2, 2, 2])