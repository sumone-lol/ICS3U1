'''
1. Write a program that asks a user how many items were on their grocery bill. 
Then ask the user to enter the cost of each item on the grocery bill. When 
the user is done, output the total cost of their groceries plus HST.
'''

item_quantity = int(input("Enter the number of items on the grocery bill: "))
cost = []
HST = 1.13

cost.append(float(input("Enter the cost of the first item: $")))
for i in range(item_quantity - 1):
    cost.append(float(input("Enter the cost of the next item: $")))
total_cost = sum(cost) * HST

print(f"The total cost of the grocery bill including HST is ${round(total_cost,2)}")