import numpy as np
from PIL import Image
from itertools import product

def generate_8x8(file):
    img = Image.open(file)
    #this may run into issues with png images
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
    return hat_img

def display_img(file,sense):
    hat_img = generate_8x8(file)
    sense.set_pixels(hat_img)
