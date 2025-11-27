'''
2. Write a function called sum_first(n) which calculates the sum of the
first n positive integers and prints the result. Assume the user entered a 
positive integer. Test your function in the main program with the following 
values for n: 0, 1, 5, 10, 50.
'''

def sum_first(n):
    sum = 0

    for i in range(1,n + 1):
        sum += i
    print(sum)

sum_first(0)
sum_first(1)
sum_first(5)
sum_first(10)
sum_first(50)