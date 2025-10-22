'''
2. The front tires of a car should both have the same pressure. Also, the rear 
tires of a car should both have the same pressure (but not necessarily the 
same pressure as the front tires.) Write a program that reads in the pressure 
of the four tires and writes a message that says if the inflation is OK or not.
'''

tire_fl = float(input("Enter the front left tire pressure\n"))
tire_fr = float(input("Enter the front right tire pressure\n"))
tire_bl = float(input("Enter the back left tire pressure\n"))
tire_br = float(input("Enter the back right tire pressure\n"))
pressure_ok = False

if (tire_fl == tire_fr) and (tire_bl == tire_br):
    pressure_ok = True

# lol no tolerance, units, or ranges
if pressure_ok:
    print("The tire pressure proportions is acceptable.")
else:
    print("The tire pressure proportions is not acceptable.")