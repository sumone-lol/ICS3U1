'''
Date: 2025-12-04

7. Write a function called play_weather that takes the string weather as a 
parameter and returns if one should play or not. If the weather is ‘sunny’ or 
‘cloudy’, then the function should return "The person should play". If the 
weather is ‘rainy’, ‘windy’ or ‘snowy’, then the function should return "The 
person should not play". If the weather is none of these, the function should 
return "It is not safe to go outside". For example, play_weather('sunny') 
should return "The person should play".
'''

# Ask user for weather
weather = input("What is the weather outside? ")

# Determine if the person should play outside
def play_weather(string):
    if string.lower() == "sunny" \
    or string.lower() == "cloudy":
        return "The person should play"
    elif string.lower() == "rainy" \
    or string.lower() == "windy" \
    or string.lower() == "snowy":
        return "The person should not play"
    else:
        return "It is not safe to go outside"

# Print the result
print(play_weather(weather))