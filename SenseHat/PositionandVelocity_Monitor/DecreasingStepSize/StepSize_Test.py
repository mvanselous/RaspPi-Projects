from sense_hat import SenseHat
from itertools import repeat
import time
import csv
import matplotlib.pyplot as plt

sense = SenseHat()

def run_test(dt,rounds):
    with open('stepsize_test_csv2','a') as f:
            write = csv.writer(f)
            write.writerow([str("Start of "+str(rounds)+" rounds"),
                            str("with dt="+str(dt))])
    for idx in range(rounds):
        print("***********\nRound: "+ str(idx)+" with dt="+str(dt))
        x = v = t = 0;
        while t <= 100:
            a =sense.accelerometer_raw['z'] - 1
            v += a*dt; x += v*dt
            t += dt
            time.sleep(dt)
        with open('stepsize_test_csv2','a') as f:
            write = csv.writer(f)
            write.writerow(["New","Run"])
            write.writerow(["v_t",str(v)])
            write.writerow(["x_t",str(x)])
        
#for dt in range(1,10):
 #   dt = dt/10
  #  run_test(dt,2)
  
run_test(.25,1)