from sense_hat import SenseHat
import time
import numpy as np
import math
import csv

sense = SenseHat()

humidity = []
idx = 0


run = True
while run:
    if idx % 30 == 0:
        val = sense.get_humidity()
        humidity.append(val)
        print(idx,val)
    for event in sense.stick.get_events():
        if event.direction == "middle":
            run = False
        else:
            continue
            
    time.sleep(1)
    idx += 1

print("done")
print(humidity)

with open('humidity_csv', 'a') as f:
    write = csv.writer(f)
    write.writerow(humidity)
    