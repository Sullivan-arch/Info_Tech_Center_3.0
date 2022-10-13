
#******************************
#Import Libraries here
from time import sleep#We imported the Sleep function from the Time library
import random#Weather condition list using the random.choice library to randomly choose a condition and storing it in its brain
#******************************


#Welcome Screen
#Developer: Sullivan Abegg
#Version: 1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is loading. 
"""


print("\033[1;34;40m  \n")#033 is the escape code, 1=Style, 32=Text color, 40m=background color
#Black-30, Red-31, Green-32, Yellow-33, Blue-34, Purple-35, Cyan-36, White-37

print("\n\nWelcome to Operation Fury Info_Tech Center")
sleep(2)
print("\033[1;33;40m \nOperation Fury's Operation System is Booting up")

for i in range(4):
    print("\033[1;35;40m OS Booting Up")
    sleep(1)


#Gas level function that tells users how much gas is left and the nearest gas
#station by using a random library
def gas_level_gauge():
    gas_level_list = ["Empty","Low","Quarter Tank","Half Tank","Three Quarters Tank","Full Tank"]
    current_gas_level = random.choice(gas_level_list)
    return current_gas_level

#Variable calling the gas_level_gauge function to store value once
gas_level_indicator = gas_level_gauge()

def list_of_gas_stations():
    gas_stations = ["Shell","Circle K","Marathon","Speedway","Meijer",]
    gas_station_nearby = random.choice(gas_stations)
    return gas_station_nearby

def gas_level_alert():
    miles_to_gas_station_low = round(random.uniform(1, 25), 1)
    miles_to_gas_station_quarter_tank = round(random.uniform(26, 50), 1)
    if gas_level_indicator == "Empty":
        print("***WARNING YOU ARE ON EMPTY***")
        sleep(1)
        print("Calling Emergency Contact")
    elif gas_level_indicator == "Low":
        sleep(1)
        print("**WARNING**")
        sleep(1)
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station.")
        sleep(1)
        print("Searching.")
        sleep(1)
        print("Searching..")
        sleep(1)
        print("Searching...")
        sleep(1)
        print("The closest gas station is", list_of_gas_stations(),"located",miles_to_gas_station_low,"miles away.")
    elif gas_level_indicator == "Quarter Tank":
        sleep(1)
        print("**WARNING**")
        sleep(1)
        print("Your gas tank is 1/4 full, checking Google Maps for the closest gas station.")
        sleep(1)
        print("Searching.")
        sleep(1)
        print("Searching..")
        sleep(1)
        print("Searching...")
        sleep(1)
        print("The closest gas station is", list_of_gas_stations(),"located",miles_to_gas_station_quarter_tank,"miles away.")
    elif gas_level_indicator == "Half Tank":
        sleep(2)
        print("Your gas tank is half full, you have enough gas to get where your going.")
    elif gas_level_indicator == "Three Quarters Tank":
        sleep(2)
        print("Your gas tank is almost full, you have enough gas to get where your going.")
    else:
        sleep(2)
        print("Your gas tank is full, you can drive anywhere with gas to spare.")






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


def weather():
    weather_forcast = ["Rain","Snow","Sunny","Windy","Foggy","Storming","Icy"]
    weather_condition = random.choice(weather_forcast)
    return(weather_condition)

weatherAlert = weather()

print("Checking weather condition.")
sleep(1)
print("Checking weather condition..")
sleep(1)
print("Checking weather condition...")
sleep(1)


def vehicle_response_system():
    if weatherAlert == "Icy":
        print("\nVRS has changed your alarm 30 minutes earlier based on the NWS forcast of",weatherAlert)
        sleep(1)
        print("VRS will only allow your car to go 30 MPH.")
    elif weatherAlert == "Snow":
        print("\nVRS has changed your alarm 15 minutes earlier based on the NWS forcast of", weatherAlert)
        sleep(1)
        print("VRS will only allow your car to go 50 MPH.")
    elif weatherAlert == "Rain":
        print("\nVRS has changed your windshield wipers to on based on the NWS forcast of", weatherAlert)
        sleep(1)
        print("VRS will only allow your car to go 65 MPH.")
    elif weatherAlert == "Windy":
        print("\nVRS has changed your alarm 5 minutes earlier based on the NWS forcast of", weatherAlert)
        sleep(1)
        print("VRS will only allow your car to go 70 MPH.")
    elif weatherAlert == "Foggy":
        print("\nVRS has changed your alarm 20 minutes earlier; Your headlights have been turned on based on the NWS forcast of", weatherAlert)
        sleep(1)
        print("VRS will only allow your car to go 40 MPH.")
    elif weatherAlert == "Storming":
        print("\nVRS has changed your alarm 15 minutes earlier; Your windshield wipers have been turned on based on the NWS forcast of", weatherAlert , )
        sleep(1)
        print("VRS will only allow your car to go 50 MPH.")
    else:
        print("\nThe weather today is", weatherAlert,"Have a great day")
        sleep(1)
        print("VRS will allow your car to go 90 MPH.")



#******************************

#Call Functions Here...
vehicle_response_system()
gas_level_alert()



