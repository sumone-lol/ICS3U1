# Name: 
# Date: 20-01-2026
# Description: An interactive lesson about natural resources

import sys
# Import functions for each page
from pages.what import page_what
from pages.how import page_how
from pages.why import page_why
from pages.depletion import page_depletion
from pages.quiz import page_quiz
from pages.worksCited import page_worksCited

# Function to collect user option given a list of valid options
def optionInput(valid):
    while True:
        option = input("Enter option: ")
        for i in valid:
            if option != i:
                continue
            else:
                return option
        print("Invalid option")

# Ask user for option
OPTIONS_MAIN = ["1", "2", "3", "q"]
print("Greeting")
print(
    """
    1) [Option 1]
    2) [Option 2]
    3) [Option 3]
    q) [Quit]
    """
)

# Collect user options and perform the appropriate action
main_menu_input = optionInput(OPTIONS_MAIN)
if main_menu_input == OPTIONS_MAIN[0]:
    print("Function 1")
    page_what()
elif main_menu_input == OPTIONS_MAIN[1]:
    print("Function 2")
elif main_menu_input == OPTIONS_MAIN[2]:
    print("Function 3")
elif main_menu_input == OPTIONS_MAIN[3]:
    print("Bye")
    sys.exit()