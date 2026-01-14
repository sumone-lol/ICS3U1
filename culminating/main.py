# Name: 
# Date: 20-01-2026
# Description: An interactive lesson about natural resources

import random
import sys
import functions

def page_mainMenu():
    # Prompt user for option and collect input
    OPTIONS_MAIN = ["1", "2", "3", "q"]
    print("Greeting")
    functions.optionTooltips(OPTIONS_MAIN, \
        ["Option 1",
        "Option 2",
        "Option 3",
        "Quit"])

    main_menu_input = functions.optionInput(OPTIONS_MAIN)
    if main_menu_input == OPTIONS_MAIN[0]:
        page_what()
    elif main_menu_input == OPTIONS_MAIN[1]:
        print("Function 2")
    elif main_menu_input == OPTIONS_MAIN[2]:
        print("Function 3")
    elif main_menu_input == OPTIONS_MAIN[3]:
        print("Bye")
        sys.exit()

def page_worksCited():
    print("\n", "-"*20, "\n")

    # Print text entry from worksCited.txt
    print("Works Cited\n")
    with open("pages/worksCited.txt") as f:
        print(f.read())
    
    print("\n", "-"*20, "\n")

    # Prompt for navigation options
    OPTIONS = ["1", "q"]
    functions.optionTooltips(OPTIONS, \
        ["Main Menu", "Quit"])

    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[1]:
        print("Bye")
        sys.exit()

def page_what():
    print("\n", "-"*20, "\n")

    # Print text entry from what.txt
    print("What are Natural Resources?\n")
    with open("pages/what.txt") as f:
        print(f.read())
    
    print("\n", "-"*20, "\n")

    # Prompt for navigation options
    OPTIONS = ["1", "2", "3", "q"]
    functions.optionTooltips(OPTIONS, \
        ["Previous",
        "Next",
        "Main Menu",
        "Quit"])

    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[1]:
        page_obtaining()
    elif main_menu_input == OPTIONS[2]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[3]:
        print("Bye")
        sys.exit()

def page_obtaining():
    print("\n", "-"*20, "\n")

    # Print text entry from obtaining.txt
    print("How can natural resources be obtained?\n")
    with open("pages/obtaining.txt") as f:
        print(f.read())
    
    print("\n", "-"*20, "\n")

    # Prompt for navigation options
    OPTIONS = ["1", "2", "3", "q"]
    functions.optionTooltips(OPTIONS, \
        ["Previous",
        "Next",
        "Main Menu",
        "Quit"])

    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_what()
    elif main_menu_input == OPTIONS[1]:
        page_why()
    elif main_menu_input == OPTIONS[2]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[3]:
        print("Bye")
        sys.exit()

def page_why():
    print("\n", "-"*20, "\n")

    # Print text entry from why.txt
    print("Why are natural resources important in society?\n")
    with open("pages/why.txt") as f:
        print(f.read())
    
    print("\n", "-"*20, "\n")

    # Prompt for navigation options
    OPTIONS = ["1", "2", "3", "q"]
    functions.optionTooltips(OPTIONS, \
        ["Previous",
        "Next",
        "Main Menu",
        "Quit"])

    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_obtaining()
    elif main_menu_input == OPTIONS[1]:
        page_depletion()
    elif main_menu_input == OPTIONS[2]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[3]:
        print("Bye")
        sys.exit()

def page_depletion():
    print("\n", "-"*20, "\n")

    # Print text entry from depletion.txt
    print("Are we running out of natural resources?\n")
    with open("pages/depletion.txt") as f:
        print(f.read())
    
    print("\n", "-"*20, "\n")

    # Prompt for navigation options
    OPTIONS = ["1", "2", "3", "q"]
    functions.optionTooltips(OPTIONS, \
        ["Previous",
        "Next",
        "Main Menu",
        "Quit"])

    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_obtaining()
    elif main_menu_input == OPTIONS[1]:
        page_quiz()
    elif main_menu_input == OPTIONS[2]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[3]:
        print("Bye")
        sys.exit()

def page_quiz():
    print("\n", "-"*20, "\n")

    # Initialize quiz answers and scores
    user_answers = []
    correct_answers = ("a", "b", "c", "d")
    score = 0

    # Prompt user for answers
    print("Question 1: ahciskmhfsfe")
    user_answers.append(input("Enter your answer: "))
    print("Question 2: ahciskmhfsfe")
    user_answers.append(input("Enter your answer: "))
    print("Question 3: ahciskmhfsfe")
    user_answers.append(input("Enter your answer: "))
    print("Question 4: ahciskmhfsfe")
    user_answers.append(input("Enter your answer: "))

    # Score calculation
    for i in range(len(user_answers)):
        if user_answers[i].lower() == correct_answers[i]:
            score += 1

page_mainMenu()