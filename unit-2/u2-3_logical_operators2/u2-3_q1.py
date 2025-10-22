'''
1. A bank has the following rule: if a customer has more than $1000 dollars in
their checking account or more than $1500 dollars in their savings account,
then there is no service charge for writing checks. Otherwise there is a $0.15
charge per check. Write a program that asks for the balance in each account
and then writes out the service charge.
'''

balance_chequing = float(input("Enter the balance of your chequing account\n"))
balance_savings = float(input("Enter the balance of your savings account\n"))

if (balance_chequing > 1000) or (balance_savings > 1500):
    service_fee = 0
else:
    service_fee = 0.15

print("The service charge is $" + service_fee)