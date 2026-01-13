# Name: 
# Date: 20-01-2026
# Description: The What page for an interactive lesson about natural resources

def page_what():
    print("What are Natural Resources?\n")
    with open("pages/what.txt") as f:
        print(f.read())