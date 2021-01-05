import numpy as np
from PIL import Image
from sense_hat import SenseHat
from itertools import product

sense = SenseHat()
sense.set_rotation(90); sense.low_light = True

img_dict = {'blinky':"Blinky.jpeg",
            'mushroom_old':"Mushroom.jpeg",
            'mushroom_new': "Mushroom_2.png",
            'mario_logo':"mario_logo.jpeg",
            'mspacman':",mspacman.jpeg",
            'bear':"bear2.jpeg"}
img = Image.open(img_dict['mario_logo'])
np_img = np.array(img)
x,y, _ = np_img.shape
stop_x,stop_y = int(np.floor(x/8)), int(np.floor(y/8))
hat_img = []

for row,col in product(range(0,8),repeat=2):
    pixel = []
    for colour in range(0,3):
        val = int(np.floor(np.average(np_img[stop_x*row:stop_x*(row+1),
                           stop_y*col:stop_y*(col+1),colour])))
        pixel.append(val)
    hat_img.append(pixel)
    
sense.set_pixels(hat_img)