# Write programs to accomplish each task.
# Determine if two given integers are both positive, both negative, or one 
# positive and one negative.

num1 = int(input("Enter an integer\n"))
num2 = int(input("Enter another integer\n"))

if num1 > 0: # haha decision tree
    if num2 > 0:
        print("both pos")
    if num2 < 0:
        print("num1+ num2-")
elif num1 < 0:
    if num2 > 0:
        print("num1- num2+")
    if num2 < 0:
        print("both neg")
else:
    print("bro really put zero lol")