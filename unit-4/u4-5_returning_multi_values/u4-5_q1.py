'''
1. Write a function called get_names() that prompts the user to enter their 
first and last names. Return the first name and last name to the main program.
Test this function in the main program and print the user’s full name.
'''

def get_names():
    first_name = input("Enter your first name: ")
    last_name = input("Enter your last name: ")

    return first_name, last_name

first_name, last_name = get_names()

print(first_name, last_name)