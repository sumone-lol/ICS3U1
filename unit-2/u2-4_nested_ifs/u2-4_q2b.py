# Write two different programs to simplify the following sequence so that the 
# effect is the same but fewer comparisons are required. Use nested ifs in one 
# of the programs and elif in the other.
'''
if (temperature > MAX_TEMP):
    print("Porridge too hot")
if (temperature < MIN_TEMP):
    print("Porridge too cold")
if (temperature <= MAX_TEMP) and (temperature >= MIN_TEMP):
    print("Porridge just right - eat it all up.")
'''

temperature = input()
MAX_TEMP = 50
MIN_TEMP = 20

if temperature > MAX_TEMP:
    print("Porridge too hot")
elif temperature < MIN_TEMP:
    print("Porridge too cold")
else:
    print("Porridge just right - eat it all up.")