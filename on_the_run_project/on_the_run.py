# Name: 
# Date: 2025-10-14
# Course: ICS3U1-13
# Description: A ticket ordering application that provides ticket prices for 
# a concert and calculates the total cost given the number of tickets

# Constants to store the ticket tier prices, HST, service charge and names
PLATINUM_PRICE = 150.00
GOLD_PRICE = 120.50
RED_PRICE = 80.75
GREEN_PRICE = 50.25
HST = 0.13
SERVICE_COST = 12.50
PRICE = "Price ($)"

# Show title and prices
print("Jay Z and Beyonc\u00e9: On the Run Tour\nTicket Prices\n___\n")
print(f"Section {PRICE:>40}")
print(f"Platinum{PLATINUM_PRICE:>40}")
print(f"Gold    {GOLD_PRICE:>40}")
print(f"Red     {RED_PRICE:>40}")
print(f"Green   {GREEN_PRICE:>40}")
print("___\n")

# Ask user for number of tickets
platinum_tickets = int(input("Enter the number of platinum tickets:  "))
gold_tickets = int(input("Enter the number of gold tickets:  "))
red_tickets = int(input("Enter the number of red tickets:  "))
green_tickets = int(input("Enter the number of green tickets:  "))
print("___\n")

# Calculate the costs
subtotal = \
    platinum_tickets * PLATINUM_PRICE + \
    gold_tickets * GOLD_PRICE + \
    red_tickets * RED_PRICE + \
    green_tickets * GREEN_PRICE
hst_fee = round(subtotal * HST, 2)
service_fee = SERVICE_COST * \
    (platinum_tickets + gold_tickets + red_tickets + green_tickets)
total = round(subtotal + hst_fee + service_fee, 2)

# Show the calculated costs
print(f"Subtotal:        {subtotal:>40}")
print(f"HST:             {hst_fee:>40}")
print(f"Service Fees:    {service_fee:>40}")
print(f"Total:           {total:>40}")
print("___\n")

# Ask for payment
print("How will you be paying?\n")
print("1 - VISA")
print("2 - MasterCard")
print("3 - American Express\n")

payment_method = int(input("Enter the payment method:  "))
name = input("Enter your name:  ")
card_num = int(input("Enter the 16-digit card number:  "))
card_expiry = int(input("Enter the card expiry date (mmyyyy):  "))

print(f"\nYour order has been processed.\nThank you for purchasing, {name}!")