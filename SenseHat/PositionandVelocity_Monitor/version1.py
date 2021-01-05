from sense_hat import SenseHat
from itertools import repeat
import time
import csv
import matplotlib.pyplot as plt

sense = SenseHat()
a_t = []
v_t = []
x_t = []

x = v = 0; step = 0; dt = 0.01
while step <= 5000:
    step += 1
    time.sleep(dt)
    a =sense.accelerometer_raw['z'] - 1
    #need to offset the force of gravity.
    v += a*dt
    x += v*dt
    print("Position:", x, ", Velocity:", v, ", Acceleration:", a)
    a_t.append(a)
    v_t.append(v)
    x_t.append(x)
    
with open('movement_csv','a') as f:
    write = csv.writer(f)
    write.writerow(a_t)
    write.writerow(v_t)
    write.writerow(x_t)
    write.writerow(['New','Run'])

#plt.plot(data)