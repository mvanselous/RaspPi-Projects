from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
import signal
import time
#Desipite its use in the SenseHat documantation, using signal is a bad practice!
#Its effect are unspecified in a multithreaded enviorment.

x = 3
y = 3
sense = SenseHat()
sense.low_light = True

def clamp(value, min_value=0, max_value=7):
    return min(max_value, max(min_value, value))

def pushed_up(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y - 1)

def pushed_down(event):
    global y
    if event.action != ACTION_RELEASED:
        y = clamp(y + 1)

def pushed_left(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x - 1)

def pushed_right(event):
    global x
    if event.action != ACTION_RELEASED:
        x = clamp(x + 1)

def refresh():
    sense.clear()
    sense.set_pixel(x, y, 100, 200, 200)

sense.stick.direction_up = pushed_up
sense.stick.direction_down = pushed_down
sense.stick.direction_left = pushed_left
sense.stick.direction_right = pushed_right
sense.stick.direction_any = refresh
refresh()

def my_alarm(signum,frame):
    print('alarm')
    sense.set_rotation(90)
    sense.show_message('SIGALRM')
    sense.set_rotation(0)
    #global x,y
    refresh()
    time.sleep(2)

def my_interupt(signum,frame):
    signal.alarm(0)
    #or
    #signal.signal(signal.SIGALRM, signal.SIG_IGN)
    sense.show_message("Control + C was pressed.",scroll_speed=0.025)
    
    
signal.signal(signal.SIGALRM, my_alarm)
signal.signal(signal.SIGINT, my_interupt)

signal.alarm(5)
signal.pause()
sense.clear()
print("test")