# Name: 
# Date: 20-01-2026
# Description: An interactive lesson about natural resources

import random
import datetime
import time
import sys
import functions

# Configurable options
TOOLTIP_DELAY = 0.5 # Seconds

def page_mainMenu():
    # Prompt user for option
    OPTIONS = ["1", "2", "3", "q"]
    print("ICS3U1 Culminating")
    print("Welcome to my interactive lesson about natural resources!\n")
    functions.optionTooltips(OPTIONS, [ \
        "Start lesson",
        "Skip to page",
        "Works cited",
        "Quit"
        ])

    # Collect input
    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_what()
    elif main_menu_input == OPTIONS[1]:
        page_selectMenu()
    elif main_menu_input == OPTIONS[2]:
        page_worksCited()
    elif main_menu_input == OPTIONS[3]:
        print("Thanks for reading!")
        sys.exit()

def page_selectMenu():
    # Prompt user for option
    OPTIONS = ["1", "2", "3", "4", "5", "b"]
    functions.optionTooltips(OPTIONS, [ \
        "What are natural resources?",
        "Obtaining natural resources",
        "Why are natural resources impotrant?",
        "Are we running out?",
        "Quiz!",
        "Back"
        ])

    # Collect input
    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_what()
    elif main_menu_input == OPTIONS[1]:
        page_obtaining()
    elif main_menu_input == OPTIONS[2]:
        page_why()
    elif main_menu_input == OPTIONS[3]:
        page_depletion()
    elif main_menu_input == OPTIONS[4]:
        page_quiz()
    elif main_menu_input == OPTIONS[5]:
        page_mainMenu()

def page_worksCited():
    print("\n", "-"*20, "\n")

    # Print text entry from worksCited.txt
    print("Works Cited\n")
    with open("pages/worksCited.txt") as f:
        print(f.read())
    
    print()
    time.sleep(TOOLTIP_DELAY)

    # Prompt for navigation options
    OPTIONS = ["1", "q"]
    functions.optionTooltips(OPTIONS, \
        ["Main Menu", "Quit"])

    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[1]:
        print("Thanks for reading!")
        sys.exit()

def page_what():
    print("\n", "-"*20, "\n")

    # Print the text entry from what.txt
    print("What are Natural Resources?\n")
    with open("pages/what.txt") as f:
        print(f.read())
    
    print()
    time.sleep(TOOLTIP_DELAY)

    # Prompt for navigation options
    OPTIONS = ["1", "2", "3", "q"]
    functions.optionTooltips(OPTIONS, [ \
        "Previous - Main menu",
        "Next - Obtaining natural resources",
        "Main Menu",
        "Quit"
        ])

    # Collect input
    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[1]:
        page_obtaining()
    elif main_menu_input == OPTIONS[2]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[3]:
        print("Thanks for reading!")
        sys.exit()

def page_obtaining():
    print("\n", "-"*20, "\n")

    # Print the text entry from obtaining.txt
    print("How can natural resources be obtained?\n")
    with open("pages/obtaining.txt") as f:
        print(f.read())
    
    print()
    time.sleep(TOOLTIP_DELAY)

    # Prompt for navigation options
    OPTIONS = ["1", "2", "3", "q"]
    functions.optionTooltips(OPTIONS, [ \
        "Previous - What are natural resources?",
        "Next - Importance of natural resources",
        "Main Menu",
        "Quit"
        ])

    # Collect input
    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_what()
    elif main_menu_input == OPTIONS[1]:
        page_why()
    elif main_menu_input == OPTIONS[2]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[3]:
        print("Thanks for reading!")
        sys.exit()

def page_why():
    print("\n", "-"*20, "\n")

    # Print the text entry from why.txt
    print("Why are natural resources important in society?\n")
    with open("pages/why.txt") as f:
        print(f.read())
    
    print()
    time.sleep(TOOLTIP_DELAY)

    # Prompt for navigation options
    OPTIONS = ["1", "2", "3", "q"]
    functions.optionTooltips(OPTIONS, [ \
        "Previous - Obtaining natural resources",
        "Next - Are we running out?",
        "Main Menu",
        "Quit"
        ])

    # Collect input
    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_obtaining()
    elif main_menu_input == OPTIONS[1]:
        page_depletion()
    elif main_menu_input == OPTIONS[2]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[3]:
        print("Thanks for reading!")
        sys.exit()

def page_depletion():
    print("\n", "-"*20, "\n")

    # Print the text entry from depletion.txt
    print("Are we running out of natural resources?\n")
    with open("pages/depletion.txt") as f:
        print(f.read())
    
    print()
    time.sleep(TOOLTIP_DELAY)

    # Prompt for navigation options
    OPTIONS = ["1", "2", "3", "q"]
    functions.optionTooltips(OPTIONS, [ \
        "Previous - Importance of natural resources",
        "Next - Quiz!",
        "Main Menu",
        "Quit"
        ])

    # Collect input
    main_menu_input = functions.optionInput(OPTIONS)
    if main_menu_input == OPTIONS[0]:
        page_why()
    elif main_menu_input == OPTIONS[1]:
        page_quiz()
    elif main_menu_input == OPTIONS[2]:
        page_mainMenu()
    elif main_menu_input == OPTIONS[3]:
        print("Thanks for reading!")
        sys.exit()

def page_quiz():
    print("\n", "-"*20)
    print("Time for a quiz!")
    time.sleep(1)

    # Initialize quiz questions, answers, and score
    # I'm avoiding text-input answers because of ambiguity
    score = 0
    user_answers = []
    correct_answers = ("b", "a", "a", "bcd", "d", "b", "b", "a")
    with open("pages/quiz.txt") as f:
        questions = f.readlines()

    # Ask questions and prompt user for answers
    for i in range(len(correct_answers)):
        time.sleep(TOOLTIP_DELAY)
        print("\n" + questions[i * 2])
        print(questions[i * 2 + 1].replace("\\n", "\n"))
        user_answers.append(input("Enter your answer: ").strip().lower())

    # Score calculation
    for i in range(len(user_answers)):
        if user_answers[i].lower() == correct_answers[i]:
            score += 1
    
    # Write results to timestamped log file
    def quiz_log():
        with open(f"quiz_{datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}.log", "a") as f:
            f.write(f"Score: {score} / {len(user_answers)}\n\n")
            for i in range(len(correct_answers)):
                f.write(questions[i * 2])
                f.write(questions[i * 2 + 1].replace("\\n", "\n"))
                f.write(f"Your answer: {user_answers[i]}\n")
                f.write(f"Correct answer: {correct_answers[i]}\n")
                f.write("\n----------\n\n")
    
     # I might add an option to make logging optional later...
    quiz_log()
    time.sleep(TOOLTIP_DELAY)
    print(f"\nScore: {score}")
    print("A log of your quiz results was created in the root folder!")
    print("\n" + "-"*10 + "\n")
    page_mainMenu()

# Initialize the program at the main menu
page_mainMenu()