'''
3. Write a program that prompts the user for their full address, one piece of 
information at a time, and save each piece of information in a different 
variable. Use the following variables: street_number, street_name, city, 
province, and postal_code. Make sure your output is nicely formatted, as it 
might appear on an envelope for mailing.
'''

province = input("What is your province of residence?\n")
city = input("What is your city of residence?\n")
street_name = input("What street do you live on?\n")
street_number = input("What is your street number?\n")
postal_code = input("What is your postal code?\n")

print(postal_code,
      street_number + " " + street_name,
      city + ", " + province,
      sep="\n")