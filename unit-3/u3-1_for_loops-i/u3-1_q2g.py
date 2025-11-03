# Use for loops to accomplish each task
# Display all integers between m and n, with step s, as determined by the user

m = int(input("Enter the start value"))
n = int(input("Enter the stop value"))
s = int(input("Enter the step value"))

for i in range(m, n, s):
    print(i)