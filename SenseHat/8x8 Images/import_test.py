from sense_hat import SenseHat
from create_8x8 import *
import time

sense = SenseHat()
sense.set_rotation(90); sense.low_light = True

sense.show_message("display_img",scroll_speed = 0.05)
display_img("images/mario3.jpeg",sense)

time.sleep(2)
sense.show_message("generate_8x8",scroll_speed = 0.05)
hat_img = generate_8x8("images/mspacman.jpeg")
sense.set_pixels(hat_img)

time.sleep(2)
sense.clear()