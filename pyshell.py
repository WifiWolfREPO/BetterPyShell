# Import some fresh libs

import datetime
import os
import platform

# Loop through the lines on the config file and save them to a list

configfile = open("config.txt", "r")

config = []

for line in configfile:
    config.append(line.strip())

configfile.close()

# Welcome message

if config[4] == "true":
    print(str(config[5].format(username=str(os.getlogin()), computer=str(platform.node()), machineos=str(platform.system()), timeandsec=str(datetime.datetime.now().strftime("%H:%M:%S")), timenosecs=str(datetime.datetime.now().strftime("%H:%M")))))

# Loop to get input

while True:
    if config[2] == "true":
        for _ in range(int(config[3])): # Skip lines if enabled on config file
            print("")

    try:        # Execute input (All this mess is from format that I dont know how to fix)
        exec(input(config[0].format(username=str(os.getlogin()), computer=str(platform.node()), machineos=str(platform.system()), timeandsec=str(datetime.datetime.now().strftime("%H:%M:%S")), timenosecs=str(datetime.datetime.now().strftime("%H:%M")))+" "))
    except Exception as error:      # Error message system (Again, format mess)
        print(config[1].format(username=str(os.getlogin()), computer=str(platform.node()), machineos=str(platform.system()), timeandsec=str(datetime.datetime.now().strftime("%H:%M:%S")), timenosecs=str(datetime.datetime.now().strftime("%H:%M")))+" "+str(error))

# I really do not know how to fix this format mess.
