'''
4. Write a program that prompts the user for a 4-digit positive integer value 
(e.g., from 1000 to 9999). Use integer division by 1000 to isolate the first 
digit. Use the remainder to isolate the remaining three digits. Repeat this 
process using division by 100, 10, and 1 to isolate the remaining digits. The 
goal of the program is to output the list of digits.
'''

num = int(input("Enter a 4-digit positive integer\n"))

digit1 = num // 1000
digit2 = num % 1000 // 100
digit3 = num % 100 // 10
digit4 = num % 10

print(digit1, digit2, digit3, digit4, sep="-")