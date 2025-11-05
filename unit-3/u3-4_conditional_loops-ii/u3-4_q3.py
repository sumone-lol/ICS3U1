'''
3. Determine the largest of n positive integers. The program should loop until 
a negative value is read. Modify the program above to find the two largest 
integers.
'''

integers = [0]

while integers[-1] >= 0:
    integers.append(int(input("Enter a positive integer, or "
                              "enter a negative integer to end the program: ")))
integers.pop()
largest1 = max(integers)
integers.remove(largest1)
largest2 = max(integers)

print(f"The largest integer is {largest1} and the second largest is {largest2}.")