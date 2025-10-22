'''
2. Ask the user their name. Give a different message depending on whether they
enter your name or another name
'''

name = input("Enter your name\n")

if name == "your name or another name":
    print("congrats")
elif name == "your name":
    print("lol")
elif name == "another name":
    print(":)")
else:
    print("bruh")