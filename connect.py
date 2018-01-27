#!/usr/bin/python

import subinitial.stacks as stacks
from time import sleep

core = stacks.Core(host="192.168.1.49")

analogdeck = stacks.AnalogDeck(core, bus_address=2)

# Change leds for no reason
for i in range(0,3):
    for j in range(16,255):

        core.rgbled.set(int(("0x00FFFF" + hex(j)[2:]), 16))
        analogdeck.rgbled.set(int(("0x00FFFF" + hex(j)[2:]), 16))
        sleep(1 / 1000)

    for j in reversed(range(16,255)):

        core.rgbled.set(int(("0x00FFFF" + hex(j)[2:]), 16))
        analogdeck.rgbled.set(int(("0x00FFFF" + hex(j)[2:]), 16))
        sleep(1 / 1000)

for i in range(0,4):
    core.rgbled.set(core.rgbled.COLOR_GREEN)
    analogdeck.rgbled.set(0)

    sleep(100/ 1000)

    core.rgbled.set(0)
    analogdeck.rgbled.set(analogdeck.rgbled.COLOR_GREEN)

    sleep(100/ 1000)



# Set the RGBs to green when done "initializing"
core.rgbled.set(core.rgbled.COLOR_GREEN)
analogdeck.rgbled.set(analogdeck.rgbled.COLOR_GREEN)

#
# while 1:
#
#     # Read input from user
#     input = readline()
#
#     if(input[1] == "engage" || 1)
#         analogdeck.solenoiddrivers.engage(input[0])
#     else if (input[1] == "disengage" || 0)
#         analogdeck.solenoiddrivers.disengage(input[0])
