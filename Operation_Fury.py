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
    weather_forcast = ["Rain","Snow","Sunny","Windy","Foggy","Storming","Icy"]
    weather_condition = random.choice(weather_forcast)
    return(weather_condition)

weatherAlert = weather()


def vehicle_response_system():
    if weatherAlert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)
        print("VRS will only allow your car to go 30 MPH")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 50 MPH")
    elif weatherAlert == "Rain":
        print("\nVRS has changed your windshield wipers to on based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 65 MPH")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 70 MPH")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your alarm 20 minutes earlier; Your headlights have been turned on based on the NWS forcast of", weatherAlert)
        print("VRS will only allow your car to go 40 MPH")
    elif weatherAlert == "Storming":
        print("\nVRS has changed your alarm 15 minutes earlier; Your windshield wipers have been turned on based on the NWS forcast of", weatherAlert , )
        print("VRS will only allow your car to go 50 MPH")
    else:
        print("\nThe weather today is", weatherAlert,"Have a great day")
        print("VRS will allow your car to go 90 MPH")

vehicle_response_system()

