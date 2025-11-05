'''
1. Repeatedly prompt the user to enter as many strings as they like. If the 
entered string is “quit”, then print “Goodbye!” and terminate the program. If 
it is any other string, print it to the screen.
'''

text = ""

while text != "quit":
    text = input('Enter a message to echo (or "quit" to exit):')
    print(text)
print("Goodbye!")