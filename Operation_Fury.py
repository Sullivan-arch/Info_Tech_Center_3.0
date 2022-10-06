#Weather
#Developer:Sullivan Abegg
#Version 1.0

"""
Create a function for our current weather using the
random.choice function to determine what the weather
is picking from a list - using If, elif & Else statements
to check the condition and print a specific corresponding
print line
"""

#import Libraries here
import random

#Weather condition list using the random.choice library
#to randomly choose a condition and storing it in its brain
def weather():
    weather_forcast = ["Rain","Snow","Sunny","Cloudy","Foggy","Storming","Icy"]
    weather_condition = random.choice(weather_forcast)
    return(weather_condition)

