'''
1. a) Create a program that checks user name and password. Think carefully how 
you want to handle each of these (i.e., you don't want to give invalid users 
information they could use to hack into the system!). Start with a single user.
b) Add one or two additional users to your system.
c) Add a security feature where there are a maximum number of failed attempts 
before the system locks out the login process.
'''

users = ["user1","user2"]
passwords = ["pass1","pass2"]
attempts = 1

user_field = input("Enter your username: ")
password_field = input("Enter your password: ")
user_index = users.index(user_field)

while password_field != passwords[user_index] and attempts <= 3:
    print("Invalid credentials. Try again.")
    attempts += 1

    user_field = input("Enter your username: ")
    password_field = input("Enter your password: ")
    user_index = users.index(user_field)

if attempts > 3:
    print("Too many failed attempts")
else:
    print("Login successful.")
