'''
2. Write a program that asks two questions: first name and last name. The 
program should then output this information with the last name printed first. 
For example, if the user entered "Fred" and "Flintstone", the output would be 
"Flintstone, Fred"
'''

first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

print(last_name + ",", first_name)