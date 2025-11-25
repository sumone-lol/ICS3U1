'''
4. Write a function called check_name(), which will keep asking for YOUR name
(looping). When you give your name, the function will exit and return control 
to the main program. This function shouldn’t print anything. Call this 
function in the main part of your program in order to test it
'''

def check_name():
    name = ""
    
    while name != "Rick":
        name = input("Enter your name: ")
        continue

check_name()
print("Finished check_name")