'''
5. Ask the user three math problems and (a) tell them if they are right, or (b)
show them the correct answer
'''

question1 = int(input("6 + 7 = "))
if question1 == 13:
    print("Correct!\n")
else:
    print("Incorrect (13)\n")

question2 = int(input("7 x 27 = "))
if question2 == 189:
    print("Correct!\n")
else:
    print("Incorrect (189)\n")

question3 = input(
    "Given the quadratic function f(x) = -5x^2 + 20x + 25, what is the "
    "equation for the axis of symmetry?\n").replace(" ","")
if question3 == "x=2":
    print("Correct!")
else:
    print("Incorrect (x = 2)")