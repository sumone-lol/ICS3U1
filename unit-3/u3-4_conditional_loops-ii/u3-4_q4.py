'''
4. Ask the user for a (small) number (n) and a word, and then display the word 
n-times on the same line. Do this until the user enters the word "done”. 
Modify the program to let the user decide which word should terminate the 
program.
'''

word = ""
n = 0
end = input("Enter a keyword to end the program: ")

while word != end:
    word = input("Enter a word to repeat: ")
    if word == end:
        break
    n = int(input("How many times should the word be repeated?: "))
    print((word + " ") * n)
