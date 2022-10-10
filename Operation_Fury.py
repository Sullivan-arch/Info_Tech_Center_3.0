#Gasoline
#Programmer:Sullivan Abegg
#Version 1.0

"""
Define a function to check our gas gauge and determine how
far we have until we need gasoline based on an if, elif, else condition
"""

#import library here
import random

#Gas level function
def gas_level_gauge():
    gas_level_list = ["Empty","Low","Quarter Tank","Half Tank","Three Quarters Tank","Full Tank"]
    current_gas_level = random.choice(gas_level_list)
    return current_gas_level

