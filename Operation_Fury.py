#Gasoline
#Programmer:Sullivan Abegg
#Version 1.0

"""
Define a function to check our gas gauge and determine how
far we have until we need gasoline based on an if, elif, else condition
"""

#import library here
import random
from time import sleep


#Gas level function
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
        print("Your gas tank is extremely low, checking Google Maps for the closest gas station")
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
        print("Your gas tank is 1/4 full, checking Google Maps for the closest gas station")
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
        print("Your gas tank is half full, you have enough gas to get where your going")
    elif gas_level_indicator == "Three Quarters Tank":
        sleep(2)
        print("Your gas tank is almost full, you have enough gas to get where your going")
    else:
        sleep(2)
        print("Your gas tank is full, you can drive anywhere with gas to spare")



gas_level_alert()