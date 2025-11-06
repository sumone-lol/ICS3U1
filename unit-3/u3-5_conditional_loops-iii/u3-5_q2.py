'''
2. Collatz Conjecture: Start with any natural number, N (1, 2, 3, 4, ...). If 
the number is even, divide it by 2. If the number is odd, multiply by 3 then 
add 1. If you repeat this process enough times, the number should always 
reach 1. Write a program that tests this conjecture by allowing the user to 
enter a number, and then apply the Collatz algorithm until the number 
reaches 1. Show the result of each step and how many iterations it took
to get to 1.
'''

number = int(input("Enter a natural number (integer > 0): "))
steps = 0

print(f"\n{number}")
while number != 1:
    if number % 2 == 0:
        number = int(number / 2)
    else:
        number = number * 3 + 1
    print(number)
    steps += 1

print(f"\nIterations: {steps}")