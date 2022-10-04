#Welcome Screen
#Developer: Sullivan Abegg
#Version: 1.0

"""
Our Welcome Screen will start our program letting
drivers know that the InfoTechCenter OS is loading. 
"""
#Import Libraries here
from time import sleep#We imported the Sleep function from the Time library

print("\033[1;34;40m  \n")#033 is the escape code, 1=Style, 32=Text color, 40m=background color
#Black-30, Red-31, Green-32, Yellow-33, Blue-34, Purple-35, Cyan-36, White-37

print("\n\nWelcome to Operation Fury Info_Tech Center")

sleep(2)

print("\033[1;33;40m \nOperation Fury's Operation System is Booting up")

print("")