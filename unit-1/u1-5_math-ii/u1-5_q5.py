'''
5. Modify the above program to ask the user for a 4-digit positive integer and 
then finds and prints the sum of the digits of the number
'''

num = int(input("Enter a 4-digit positive integer\n"))

digit1 = num // 1000
digit2 = num % 1000 // 100
digit3 = num % 100 // 10
digit4 = num % 10

num_digits_sum = digit1 + digit2 + digit3 + digit4
print(f"{digit1} + {digit2} + {digit3} + {digit4} =", num_digits_sum)