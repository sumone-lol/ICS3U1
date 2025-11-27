'''
1. Write a function called day_week(n) which given an integer, n, prints the
corresponding day of the week (e.g. “Monday”) or a suitable error message for 
an invalid value. Assume the user entered an integer. Test your function in 
the main program with the following values for n: 1, 7, 3, 10, 0, -1.
'''

days_list = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]

def day_week(n):
    if n > 0 and n <= len(days_list):
        print(days_list[n - 1])
    else:
        print("Enter an integer between 1 and 7")

#1, 7, 3, 10, 0, -1
day_week(1)
day_week(7)
day_week(3)
day_week(10)
day_week(0)
day_week(-1)