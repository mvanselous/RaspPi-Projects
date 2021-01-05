#!/usr/bin/python
#from sense_hat import SenseHat

#sense = SenseHat()

#red = (200, 225, 105)
#sense.show_message("I am the best, You are the worst. >:)", text_colour=red)

from sense_hat import SenseHat
import time
import numpy as np
import math

sense = SenseHat()

#sense.low_light = False
sense.low_light = True
sense.set_rotation(90)

yellow = (200, 80, 80)
blue = (80, 80, 200)

temp_old = idx = 0

while True:
    temp = math.floor(sense.temp)
    #print(idx,temp)
    if temp != temp_old:
        sense.clear(yellow)
        time.sleep(0.1)    
        pixels = [yellow if i < temp else blue for i in range(64)]
        sense.set_pixels(pixels)
        time.sleep(2)
        temp_old = temp
        sense.set_pixel(3,6,yellow)
        sense.set_pixel(6,2,blue)
    time.sleep(1)
    idx +=1