'''
6. Write a program that reads a time interval in hours, minutes, and seconds, 
and converts this measurement to hours only. Assume that the user is entering 
a reasonable number for minutes (between 0 and 59) and a reasonable number for 
seconds (between 0 and 59)
'''

unit = input("Enter the unit of time (s - seconds, m - minutes, h - hours)\n")
raw_time = float(input(f"How many {unit}?\n"))
hours_time = 0

if unit == "s":
    hours_time = raw_time / 3600
elif unit == "m":
    hours_time = raw_time / 60
elif unit == "h":
    hours_time = raw_time

print(str(raw_time) + unit, "is equivalent to", str(hours_time), "hours")