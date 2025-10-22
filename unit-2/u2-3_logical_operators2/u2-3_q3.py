'''
3. Write a program that asks a user how many boxes of cookies they want to 
order. There are three types of cookies: Chocolate Chip, Raisin, and 
Shortbread. If the user orders 5 boxes of one type or 10 boxes in total, they 
will receive a 10% discount. Write a program that outputs the total cost 
including tax. Each box of cookies cost $6.95.
Try rearranging your if statements in two different ways to make this program
work.
'''

print("Available cookies: Chocolate Chip, Raisin, Shortbread")

COOKIE_COST = 6.95
TAX = 1.13
choco_quantity = int(input("How many boxes of chocolate cookies would you like to order?\n"))
raisin_quantity = int(input("How many boxes of raisin cookies?\n"))
short_quantity = int(input("How many boxes of shortbread?\n"))
discount = 1.0

# The prompt asked for exactly 5 and 10, not more than. sorry lol can't buy more :shrug:
if (choco_quantity == 5) \
    or (raisin_quantity == 5) \
    or (short_quantity == 5) \
    or (choco_quantity + raisin_quantity + short_quantity == 10):
        discount = 0.9

total_cost = (choco_quantity + raisin_quantity + short_quantity) \
    * COOKIE_COST * TAX * discount

print("The total cost of your order is $" + total_cost)
