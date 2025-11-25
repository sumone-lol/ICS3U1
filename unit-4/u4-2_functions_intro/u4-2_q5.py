'''
5. Write a function called count_down(), which will count backwards from 10 to 
0, with a 1 second delay between printing each number on the screen. Call this
function in the main part of your program in order to test it.
'''
import time

def count_down():
    for i in range(10,-1,-1):
        print(i)
        time.sleep(1)

count_down()