
# Function to collect user option given a list of valid options
def optionInput(valid):
    while True:
        option = input("\nEnter option: ").strip().lower()
        for i in valid:
            if option != i:
                continue
            else:
                return option
        print("Invalid option")

# Function to show tooltips
def optionTooltips(keys, labels):
    for i in range(len(keys)):
        print(f"{keys[i]}) [{labels[i]}]")