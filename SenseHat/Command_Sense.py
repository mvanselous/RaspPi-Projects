#This is a simply file I created to preform quick status checks of the SenseHat.

from sense_hat import SenseHat
import time
import numpy as np
import math

sense = SenseHat()

#sense.low_light = False
sense.low_light = True
sense.set_rotation(90)

while True:
    val = input()
    exec(val)