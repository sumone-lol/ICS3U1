'''
6. Fractions are represented as an integer numerator over an integer 
denominator. Recall that improper fractions have numerator greater than 
denominator, and mixed fractions is a whole number combined with a proper 
fraction. To change an improper fraction into a mixed fraction, you can use 
integer division and the remainder operator (modulo). Write a program that 
will allow the user to enter two integer values, a numerator and denominator. 
The program should output these values as an improper fraction, and then 
output the equivalent mixed fraction
'''

numer = int(input("Enter the numerator\n"))
denom = int(input("Enter the denominator\n"))

improper_frac = f"{numer}/{denom}"
proper_frac = f"{numer // denom} {numer % denom}/{denom}"

print(f"Improper fraction: {improper_frac}")
print(f"Proper fraction: {proper_frac}")