from sense_hat import SenseHat
from itertools import repeat
import time
import csv
import matplotlib.pyplot as plt

sense = SenseHat()
data = []

step = 0
while step <= 100:
    step += 1
    time.sleep(.1)
    z =sense.accelerometer_raw['z']
    data.append(z)
    print(z)

with open('accelerometer_raw_csv','a') as f:
    write = csv.writer(f)
    write.writerow(data)

plt.plot(data)
