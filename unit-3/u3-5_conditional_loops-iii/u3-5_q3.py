'''
3. One useful technique when analyzing a number is to use a loop and the 
modulus operator to extract each digit from the end.
Consider this code:

num = int(input("Enter a positive integer: "))
while num >= 1:
    digit = num % 10
    num = num//10
    print(digit)

Use this above code to do the following:
a. Count the number of sevens in a positive integer.
b. Count the number of odd digits, and the number of even digits, in a positive integer.
c. Determine the sum of a positive integer's digits.
'''

number = str(int(input("Enter a positive integer: ")))
digits = []

for i in range(len(number)):
    digits.append(int(number[i]))
num_of_sevens = digits.count(7)
num_of_odds = \
    digits.count(1) + \
    digits.count(3) + \
    digits.count(5) + \
    digits.count(7) + \
    digits.count(9)
num_of_evens = \
    digits.count(0) + \
    digits.count(2) + \
    digits.count(4) + \
    digits.count(6) + \
    digits.count(8)
digits_sum = sum(digits)

print(f"The number of 7's is {num_of_sevens}")
print(f"The number of odd digits is {num_of_odds}")
print(f"The number of even digits is {num_of_evens}")
print(f"The sum of all digits is {digits_sum}")