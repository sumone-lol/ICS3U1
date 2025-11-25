'''
3. Write a function called print_signature(), which will print your name and 
address inside a box made up of characters. You should use the previous two 
functions as part of this program. The output might look something like:
********************
Your Name
Your Address
********************
Call this function in the main part of your program in order to test it
'''

def print_signature(name,address):
    print("="*20)
    print(name)
    print(address)
    print("="*20)

print_signature("Rick","22.4438719,-74.2230846")