from sense_emu import SenseHat
import time
import numpy as np

sense = SenseHat()

#sense.redraw = False
sense.set_rotation(90)

red = (100, 80, 20)
blue = (20, 80, 100)

#while True:
#    temp = sense.temp
#    pixels = [red if i < temp else blue for i in range(64)]
#    sense.set_pixels(pixels)
#    time.sleep(2)
#    sense.set_pixels(np.full((64,1),blue))
#    time.sleep(0.5)

temp = 46

pixels = [red if i < temp else blue for i in range(64)]
#print(pixels)

test = [blue] * 64
print(test)